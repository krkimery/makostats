from fbConsts import DATA, DATA_FILENAME, YEARS
from fbScrapeStats import get_html_for_team
import re
import pickle
from bs4 import BeautifulSoup
import time
import logging


def build_team_from_scrape(team, year):
    """get a Team object built from freshly scraped data"""
    try:
        new_team = Team(BeautifulSoup(get_html_for_team(team, year), "html.parser"))
        return new_team
    except:
        logging.warn("Failed to build team: {} {}".format(team, year))
        return None


def build_all_teams_from_scrape(year):
    '''iterate through all teams and build Team objects for each of them'''
    year_dict = {}
    for team in DATA.keys():
        year_dict[team] = build_team_from_scrape(team, year)
        time.sleep(3)
    return year_dict


def build_all_teams():
    '''loads stored Teams, builds from scrape current teams'''
    total_dict = {}
    for year in YEARS:
        total_dict.update(load_all_teams_for_year(year))
        if year in total_dict:
            continue
        else:
            new_dict = build_all_teams_from_scrape(year)
            store_data_for_year(year, {year: new_dict})
            total_dict[year] = new_dict
    return total_dict


def store_all_data():
    """Store all data to disk"""
    dict_to_be_stored = build_all_teams()
    for year in YEARS:
        store_data_for_year(year, dict_to_be_stored[year])


def store_data_for_year(year, data_dict):
    """Store the data for a given year"""
    with open(DATA_FILENAME + str(year), "wb") as f:
        pickle.dump(data_dict, f)
    logging.info("Stored data for year: {}".format(year))


def load_all_teams_for_year(year):
    '''load all of the pickled/stored teams from storage'''
    year_dict = {}
    try:
        with open(DATA_FILENAME + str(year), "rb") as f:
            year_dict.update(pickle.load(f))
            logging.info("Loaded stored data for year: {}".format(year))
    except:
        logging.info("Failed to load stored data for year: {}".format(year))

    return year_dict


class Team:

    def __init__(self, soup_obj):
        self.soup = soup_obj
        self.build_stat_attrs()
        self.build_split_attrs()
        self.build_per_game_stats()
        self.build_custom_attrs()

    def build_custom_attrs(self):
        title_regex = re.search(r"(\d{4}) (\D*\w*\D*)", self.soup.title.string)
        self.year = int(title_regex.groups()[0])
        self.team = title_regex.groups()[1]
        self.url = DATA[self.team].get("URL", 999)
        self.conference = DATA[self.team].get("Conference", "Other")
        self.Point_Differential_Per_Game = self.Scoring_Points_Per_Game-self.Defense_Scoring_Points_Per_Game
        self.Yardage_Differential_Per_Game = self.Total_Offense_Yards_Per_Game-self.Defense_Total_Offense_Yards_Per_Game
        self.Winrate =  self.Wins_All_Games/(self.Wins_All_Games+self.Losses_All_Games) \
                        if self.Wins_All_Games > 0 else 0.0
        self.FBS_Winning_Winrate = self.Wins_vs_FBS_Winning / (self.Wins_vs_FBS_Winning + self.Losses_vs_FBS_Winning) \
                                    if self.Wins_vs_FBS_Winning > 0 else 0.0

        self.FBS_Losing_Winrate = self.Wins_vs_FBS_Non_Winning / (self.Wins_vs_FBS_Non_Winning + self.Losses_vs_FBS_Non_Winning) \
                                    if self.Wins_vs_FBS_Non_Winning > 0 else 0.0

        self.Power_5_Winrate = self.Wins_vs_FBS_Power_5 / (self.Wins_vs_FBS_Power_5 + self.Losses_vs_FBS_Power_5) \
                                    if self.Wins_vs_FBS_Power_5 > 0 else 0.0

    def build_per_game_stats(self):
        total_games = self.Wins_All_Games + self.Losses_All_Games
        temp_dict = tuple(self.__dict__.iteritems())
        if total_games != 0.0:
            for attr, val in temp_dict:
                if isinstance(val, float):
                    if "_per" not in attr.lower() and "win" not in attr.lower() and "loss" not in attr.lower():
                        setattr(self, attr + "_Per_Game", val/total_games)

    def build_stat_attrs(self):
        for td in self.soup.find_all("td", class_="statistic-name"):
            attr, sub_attrs = self._get_attr_and_sub_attrs(td)
            stats = self._get_cleaned_stats_list(td)
            opponent_stats = self._get_cleaned_stats_list(td.find_next())
            full_attrs = zip( [self._clean_attr_string(attr+"_"+sub) if attr.replace("_", "") != sub
                               else self._clean_attr_string(attr) for sub in sub_attrs], stats)
            opponent_full_attrs = zip( [self._clean_attr_string("Defense_"+attr+"_"+sub) if attr.replace("_", "") != sub
                               else self._clean_attr_string("Defense_"+attr) for sub in sub_attrs], opponent_stats)
            self._set_attributes(full_attrs)
            self._set_attributes(opponent_full_attrs)

    def build_split_attrs(self):
        for td in self.soup.find_all("td", class_="split-name"):
            attr = self._get_attr_and_sub_attrs(td)[0].replace("/", "_or_")
            sub_attrs = [outcome + attr for outcome in ["Wins_", "Losses_", "Ties_"]]
            stats = self._get_cleaned_stats_list(td)
            full_attrs = zip(sub_attrs, stats)
            self._set_attributes(full_attrs)

    def _set_attributes(self, attr_names):
        for attribute, statistic in attr_names:
            setattr(self, attribute, statistic)

    def _get_attr_and_sub_attrs(self, element):
        attr = element.text.split(":")[0].replace(" ", "_").replace(".", "").replace("-", "_")
        sub_attrs = element.text.split(":")[-1].replace(" ", "").split("-")
        return attr, sub_attrs

    def _clean_attr_string(self, raw_attr):
        return raw_attr.replace("/", "_Per_").replace("%", "_Percent").replace("2", "Two")

    def _get_cleaned_stats_list(self, td):
        raw_stat_list = td.find_next().text.replace(" ", "").split("-")
        return [float(stat.replace("%", "").replace(",", "")) if stat and ":" not in stat
                else float(stat.split(":")[0]) if stat else 0.0 for stat in raw_stat_list]









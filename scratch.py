"""
    Scratch file for testing code snippets for usage in the other modules
"""

from fbScrapeStats import get_html_for_team
from bs4 import BeautifulSoup


def testy():
    return BeautifulSoup( get_html_for_team("Texas Longhorns", 2018), "html.parser")


class Team:

    def __init__(self, soup_obj):
        self.soup = soup_obj

    def build_stat_attrs(self):
        for td in self.soup.find_all("td", class_="statistic-name"):
            attr = td.text.split(":")[0].replace(" ", "_")
            subattrs = td.text.split(":")[-1].replace(" ", "").split("-")
            stats = td.find_next().text.replace(" ", "").split("-")
            full_attrs = [self._clean_attr_string(attr+"_"+sub) if attr.replace("_", "") != sub else self._clean_attr_string(attr) for sub in subattrs]
            print zip(full_attrs, stats)

    def build_split_attrs(self):
        for td in self.soup.find_all("td", class_="split-name"):
            print td.text, td.find_next().text
            attr = td.text.split(":")[0].replace(" ", "_")
            stat = td.find_next().text.replace(" ", "_")
            print td.text.replace(" ", "_").replace(":", "")
            print td.find_next().text.replace(" ", "")

    def _clean_attr_string(self, raw_attr):
        return raw_attr.replace("/", "_Per_").replace("%", "_Percent").replace("2", "Two")





#STATS
#soup.find_all("td", class_="statistic-name")
#for td in soup.find_all("td", class_="statistic-name"):
    #print td.text, td.find_next().text

    #can probably split attrs/stats based off ":" and "-"....
    #Rushing:  Attempts - Yards - TD
    #could be... self.RushingAttempts, self.RushingYards, self.RushingTD by splitting on : and - and re-combine
    #corresponding stats would need to be grouped this way as well...
    #569 - 2143 - 24
    #self.RushingAttempts=569, self.RushingYards=2143... by splitting on - again

#win/loss splits:
#for td in soup.find_all("td", class_="split-name"):
    #print td.text, td.find_next().text
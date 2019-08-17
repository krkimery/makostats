from unittest import TestCase
from makostats.fbReadStats import Team, build_all_teams, build_team_from_scrape, build_all_teams_from_scrape, store_all_data, store_data_to_json_for_year, load_all_teams_for_year, load_all_from_json, load_from_json
from makostats.fbConsts import DATA, YEARS
import json
import copy
import mock
import logging

class TestTeam(TestCase):

    def setUp(self):
        self.bama_2014_json = {"Defense_3rd_Down_Conversions_Attempts_Per_Game": 15.571428571428571, "Defense_PAT_Kicking_Attempts": 25.0, "Penalties_Number_Per_Game": 4.928571428571429, "Two_Point_Conversions_Success_Percent": 33.33, "Defense_Kickoff_Returns_TD": 1.0, "Losses_vs_FBS_(I_A)": 2.0, "Defense_Punt_Returns_Returns_Per_Game": 0.8571428571428571, "Defense_3rd_Down_Conversions_Attempts": 218.0, "3rd_Down_Conversions_Conversions": 102.0, "Passing_Completions_Per_Game": 20.714285714285715, "Defense_Total_Offense_Yards": 4598.0, "Point_Differential_Per_Game": 18.500000000000004, "Defense_Passing_Attempts": 493.0, "Defense_PAT_Kicking_Attempts_Per_Game": 1.7857142857142858, "Rushing_TD": 35.0, "Defense_Total_Offense_Yards_Per_Game": 328.42857142857144, "4th_Down_Conversions_Conversions": 10.0, "Losses_vs_Unranked_(AP)": 0.0, "Defense_Punting_Yards_Per_Game": 270.7142857142857, "Kickoff_Returns_Yards": 1006.0, "Defense_Passing_Interceptions": 11.0, "Yardage_Differential_Per_Game": 156.07142857142856, "3rd_Down_Conversions_Attempts_Per_Game": 14.214285714285714, "Defense_First_Downs_ByPenalty_Per_Game": 0.8571428571428571, "Defense_Passing_Yards": 3164.0, "Defense_Penalties_Number_Per_Game": 4.357142857142857, "Punting_Punts": 55.0, "Interceptions_TD_Per_Game": 0.0, "Defense_Kickoff_Returns_TD_Per_Game": 0.07142857142857142, "Defense_Rushing_Yards": 1434.0, "Two_Point_Conversions_Attempts": 3.0, "Defense_Rushing_Attempts_Per_Game": 32.285714285714285, "Defense_PAT_Kicking_Made_Per_Game": 1.6428571428571428, "Wins_vs_FBS_non_Power_5": 2.0, "Defense_Interceptions_Returns_Per_Game": 0.7142857142857143, "Defense_Total_Offense_Plays_Per_Game": 67.5, "Defense_4th_Down_Conversions_Attempts": 18.0, "Defense_Kickoff_Returns_Yards_Per_Return": 21.52, "Defense_Total_Offense_Plays": 945.0, "Defense_4th_Down_Conversions_Conversions": 7.0, "Losses_vs_Ranked_(AP)": 2.0, "Penalties_Yards": 562.0, "First_Downs_Passing": 170.0, "Wins_vs_Non_Conference": 4.0, "Losses_vs_BCS_non_AQ": 0.0, "Defense_Kickoff_Returns_Returns": 60.0, "Wins_on_Road_or_Neutral_Site": 5.0, "PAT_Kicking_Attempts_Per_Game": 4.642857142857143, "Wins_vs_Ranked_(AP)": 3.0, "Defense_Kickoff_Returns_Returns_Per_Game": 4.285714285714286, "Passing_TD": 32.0, "Losses_vs_FBS_Non_Winning": 0.0, "Defense_Two_Point_Conversions_Attempts": 2.0, "Red_Zone_Attempts_Per_Game": 4.571428571428571, "Defense_Red_Zone_Success_Percent": 84.09, "Defense_First_Downs_Rushing": 81.0, "Defense_Red_Zone_Attempts": 44.0, "Losses_vs_FBS_Winning": 2.0, "3rd_Down_Conversions_Attempts": 199.0, "Passing_Rating": 155.73, "Defense_Passing_Attempts_Per_Game": 35.214285714285715, "Defense_Punting_Yards": 3790.0, "Fumbles_Number": 18.0, "Scoring_Points_Per_Game": 36.92857142857143, "Defense_Fumbles_Lost_Per_Game": 0.6428571428571429, "Defense_3rd_Down_Conversions_Conversion_Percent": 37.61, "Red_Zone_Scores": 55.0, "Defense_Rushing_TD": 5.0, "Defense_Passing_Completions_Per_Game": 19.142857142857142, "Passing_Yards_Per_Game": 277.85714285714283, "year": 2014, "Defense_Field_Goals_Success_Percent": 92.0, "Defense_Field_Goals_Made_Per_Game": 1.6428571428571428, "Defense_First_Downs_Passing_Per_Game": 10.071428571428571, "Defense_Interceptions_Returns": 10.0, "Passing_Attempts": 451.0, "Fumbles_Number_Per_Game": 1.2857142857142858, "Defense_Rushing_TD_Per_Game": 0.35714285714285715, "Field_Goals_Made_Per_Game": 1.0, "Wins_in_November": 4.0, "Punting_Yards": 2640.0, "Defense_First_Downs_Total": 234.0, "Defense_Two_Point_Conversions_Made_Per_Game": 0.14285714285714285, "Rushing_Attempts": 567.0, "3rd_Down_Conversions_Conversions_Per_Game": 7.285714285714286, "Defense_Scoring_Points_Per_Game": 18.428571428571427, "Passing_Rating_Per_Game": 11.123571428571427, "Punt_Returns_Returns_Per_Game": 1.7857142857142858, "Losses_vs_BCS_AQ": 2.0, "Rushing_Yards_Per_Game": 206.64285714285714, "Defense_Passing_Rating_Per_Game": 8.323571428571428, "Defense_Passing_TD": 19.0, "3rd_Down_Conversions_Conversion_Percent": 51.26, "Defense_Punting_Punts_Per_Game": 6.285714285714286, "team": "Alabama Crimson Tide", "Defense_3rd_Down_Conversions_Conversions_Per_Game": 5.857142857142857, "Punt_Returns_Yards_Per_Game": 16.714285714285715, "Losses_vs_Conference": 1.0, "PAT_Kicking_Success_Percent": 96.9, "Defense_Red_Zone_Scores_Per_Game": 2.642857142857143, "Punt_Returns_Yards": 234.0, "Defense_Fumbles_Lost": 9.0, "Losses_in_December_or_January": 1.0, "First_Downs_ByPenalty": 16.0, "Punt_Returns_Returns": 25.0, "Penalties_Number": 69.0, "Wins_vs_FBS_Power_5": 9.0, "Defense_Scoring_Games": 14.0, "Defense_PAT_Kicking_Success_Percent": 92.0, "Total_Offense_Yards_Per_Game": 484.5, "Passing_Interceptions_Per_Game": 0.7142857142857143, "4th_Down_Conversions_Conversion_Percent": 76.92, "Scoring_Games": 14.0, "Wins_vs_FCS_(I_AA)": 1.0, "Defense_Kickoff_Returns_Yards_Per_Game": 92.21428571428571, "Defense_First_Downs_Rushing_Per_Game": 5.785714285714286, "Defense_Red_Zone_Attempts_Per_Game": 3.142857142857143, "Rushing_TD_Per_Game": 2.5, "PAT_Kicking_Made_Per_Game": 4.5, "Wins_vs_FBS_(I_A)": 11.0, "First_Downs_ByPenalty_Per_Game": 1.1428571428571428, "Red_Zone_Scores_Per_Game": 3.9285714285714284, "Two_Point_Conversions_Made": 1.0, "Wins_vs_Conference": 8.0, "Power_5_Winrate": 0.8181818181818182, "Defense_Punt_Returns_Yards_Per_Return": 6.92, "Defense_Passing_Interceptions_Per_Game": 0.7857142857142857, "conference": "SEC", "Defense_First_Downs_Total_Per_Game": 16.714285714285715, "Defense_Passing_TD_Per_Game": 1.3571428571428572, "Wins_vs_Unranked_(AP)": 9.0, "Defense_Total_Offense_Yards_Per_Play": 4.87, "Kickoff_Returns_Yards_Per_Return": 20.53, "Total_Offense_Yards": 6783.0, "Total_Offense_Plays_Per_Game": 72.71428571428571, "Scoring_Games_Per_Game": 1.0, "Red_Zone_Success_Percent": 85.94, "Interceptions_Yards_Per_Game": 6.0, "First_Downs_Rushing_Per_Game": 11.0, "Wins_vs_FBS_Winning": 9.0, "First_Downs_Total_Per_Game": 24.285714285714285, "Wins_at_Home": 7.0, "Defense_Fumbles_Number_Per_Game": 1.4285714285714286, "Defense_Field_Goals_Attempts_Per_Game": 1.7857142857142858, "Wins_in_October": 3.0, "Losses_vs_FBS_Power_5": 2.0, "Defense_Penalties_Yards": 516.0, "Defense_4th_Down_Conversions_Conversions_Per_Game": 0.5, "Defense_Field_Goals_Attempts": 25.0, "Interceptions_TD": 0.0, "Losses_vs_FBS_non_Power_5": 0.0, "Punting_Punts_Per_Game": 3.9285714285714284, "First_Downs_Total": 340.0, "Defense_Two_Point_Conversions_Made": 2.0, "Defense_Passing_Yards_Per_Game": 226.0, "Kickoff_Returns_Returns": 49.0, "Field_Goals_Success_Percent": 63.6, "Rushing_Attempts_Per_Game": 40.5, "Interceptions_Returns_Per_Game": 0.7857142857142857, "Punt_Returns_TD_Per_Game": 0.0, "FBS_Winning_Winrate": 0.8181818181818182, "Defense_First_Downs_Passing": 141.0, "Kickoff_Returns_TD": 0.0, "Defense_Two_Point_Conversions_Attempts_Per_Game": 0.14285714285714285, "Defense_Interceptions_TD": 1.0, "Kickoff_Returns_Returns_Per_Game": 3.5, "Punt_Returns_Yards_Per_Return": 9.36, "Losses_on_Road_or_Neutral_Site": 2.0, "Wins_vs_FBS_Non_Winning": 2.0, "Kickoff_Returns_Yards_Per_Game": 71.85714285714286, "Wins_All_Games": 12.0, "Defense_Punting_Yards_Per_Punt": 43.07, "4th_Down_Conversions_Conversions_Per_Game": 0.7142857142857143, "Rushing_Yards_Per_Attempt": 5.1, "Total_Offense_Yards_Per_Play": 6.66, "Punt_Returns_TD": 0.0, "Defense_3rd_Down_Conversions_Conversions": 82.0, "Defense_Punt_Returns_Returns": 12.0, "Defense_Rushing_Attempts": 452.0, "Defense_PAT_Kicking_Made": 23.0, "Defense_Rushing_Yards_Per_Game": 102.42857142857143, "Kickoff_Returns_TD_Per_Game": 0.0, "First_Downs_Passing_Per_Game": 12.142857142857142, "Defense_Interceptions_Yards_Per_Game": 8.857142857142858, "Passing_Interceptions": 10.0, "Defense_Punt_Returns_Yards": 83.0, "Winrate": 0.8571428571428571, "Defense_Fumbles_Number": 20.0, "Defense_Punt_Returns_Yards_Per_Game": 5.928571428571429, "Defense_Rushing_Yards_Per_Attempt": 3.17, "Field_Goals_Made": 14.0, "Punting_Yards_Per_Punt": 48.0, "Scoring_Points": 517.0, "Fumbles_Lost_Per_Game": 0.8571428571428571, "PAT_Kicking_Made": 63.0, "Defense_Time_of_Possession__Per__Game": 27.0, "Defense_4th_Down_Conversions_Attempts_Per_Game": 1.2857142857142858, "Rushing_Yards": 2893.0, "Losses_All_Games": 2.0, "Fumbles_Lost": 12.0, "Losses_in_November": 0.0, "Wins_vs_BCS_non_AQ": 2.0, "Defense_Passing_Rating": 116.53, "Defense_Red_Zone_Scores": 37.0, "Two_Point_Conversions_Made_Per_Game": 0.07142857142857142, "Passing_TD_Per_Game": 2.2857142857142856, "Defense_Interceptions_TD_Per_Game": 0.07142857142857142, "Passing_Yards": 3890.0, "Field_Goals_Attempts": 22.0, "Interceptions_Returns": 11.0, "Wins_in_August_or_September": 4.0, "Total_Offense_Plays": 1018.0, "PAT_Kicking_Attempts": 65.0, "Field_Goals_Attempts_Per_Game": 1.5714285714285714, "First_Downs_Rushing": 154.0, "Defense_Passing_Completions": 268.0, "Defense_Punting_Punts": 88.0, "Passing_Attempts_Per_Game": 32.214285714285715, "Defense_Penalties_Yards_Per_Game": 36.857142857142854, "Wins_vs_BCS_AQ": 9.0, "Punting_Yards_Per_Game": 188.57142857142858, "Defense_Scoring_Games_Per_Game": 1.0, "Passing_Completions": 290.0, "4th_Down_Conversions_Attempts": 13.0, "Defense_Scoring_Points": 258.0, "Defense_Kickoff_Returns_Yards": 1291.0, "Defense_Field_Goals_Made": 23.0, "Losses_at_Home": 0.0, "Time_of_Possession__Per__Game": 31.0, "Defense_Punt_Returns_TD_Per_Game": 0.0, "Penalties_Yards_Per_Game": 40.142857142857146, "Wins_in_December_or_January": 1.0, "url": 8, "4th_Down_Conversions_Attempts_Per_Game": 0.9285714285714286, "Defense_Penalties_Number": 61.0, "FBS_Losing_Winrate": 1.0, "Defense_Punt_Returns_TD": 0.0, "Red_Zone_Attempts": 64.0, "Defense_First_Downs_ByPenalty": 12.0, "Defense_Two_Point_Conversions_Success_Percent": 100.0, "Two_Point_Conversions_Attempts_Per_Game": 0.21428571428571427, "Defense_Interceptions_Yards": 124.0, "Defense_4th_Down_Conversions_Conversion_Percent": 38.89, "Interceptions_Yards": 84.0, "Losses_vs_FCS_(I_AA)": 0.0, "Losses_in_August_or_September": 0.0, "Losses_vs_Non_Conference": 1.0, "Losses_in_October": 1.0}
        self.bama = Team.load_from_json(self.bama_2014_json)

    def test_dump_to_json(self):
        self.assertEqual(json.loads(self.bama.dump_to_json()), self.bama_2014_json)

    def test_load_from_json(self):
        newTeam = Team.load_from_json({"testMethod":12, "testTwo":"dog"})
        self.assertEqual(12, newTeam.testMethod)
        self.assertEqual("dog", newTeam.testTwo)

    def test_build_per_game_stats(self):
        original_stats = copy.deepcopy(self.bama.__dict__)
        self.bama.build_per_game_stats()
        for stat, val in original_stats.iteritems():
            self.assertEqual(val, getattr(self.bama, stat))

        self.bama.test_attr = 100.0
        self.bama.Wins_All_Games = 1.0
        self.bama.Losses_All_Games = 1.0
        self.bama.build_per_game_stats()
        self.assertEqual(self.bama.test_attr_Per_Game, 50.0)



class ModuleTests(TestCase):

    @mock.patch("makostats.fbReadStats.store_data_to_json_for_year")
    @mock.patch("makostats.fbReadStats.build_all_teams_from_scrape")
    @mock.patch("makostats.fbReadStats.load_all_teams_for_year")
    def test_build_all_teams(self, mock_load, mock_build, mock_store):
        mock_load.return_value = {
                                    "2008": "fake data",
                                    "2009": "fake data",
                                    "2010": "fake data",
                                    "2011": "fake data",
                                    "2012": "fake data",
                                    "2013": "fake data",
                                    "2014": "fake data",
                                    "2015": "fake data",
                                    "2016": "fake data",
                                    "2017": "fake data",
                                    "2018": "fake data",
                                }

        results = build_all_teams()
        self.assertEqual(results, mock_load.return_value)
        self.assertFalse(mock_build.called)
        self.assertFalse(mock_store.called)

        mock_load.return_value = {2010: "fake data"}
        _ = build_all_teams()
        self.assertTrue(mock_build.called)
        self.assertEqual(mock_build.call_args[0][0], 2018)
        self.assertTrue(mock_store.called)
        self.assertEqual(mock_store.call_args[0][0], 2018)

    @mock.patch("makostats.fbReadStats.get_html_for_team")
    @mock.patch("makostats.fbReadStats.BeautifulSoup")
    @mock.patch("makostats.fbReadStats.Team")
    def test_build_team_from_scrape(self, mock_team, mock_soup, mock_get_html):
        _ = build_team_from_scrape("fake team", 2012)
        self.assertTrue(mock_get_html.called)
        self.assertEqual(mock_get_html.call_args[0][0], "fake team")

        mock_team.side_effect = [Exception,]
        self.assertIsNone(build_team_from_scrape("fake team", 2020))

    @mock.patch("time.sleep")
    @mock.patch("makostats.fbReadStats.build_team_from_scrape")
    def test_build_all_teams_from_scrape(self, mock_build, mock_sleep):
        results = build_all_teams_from_scrape(2020)
        self.assertEqual(len(DATA.keys()), len(results.keys()))
        self.assertEqual(mock_build.call_args[0][1], 2020)

    @mock.patch("makostats.fbReadStats.store_data_to_json_for_year")
    @mock.patch("makostats.fbReadStats.build_all_teams")
    def test_store_all_data(self, mock_build, mock_store):
        store_all_data()
        self.assertTrue(mock_store.called)


    @mock.patch("makostats.fbReadStats.open")
    @mock.patch("makostats.fbReadStats.json.dump")
    @mock.patch("makostats.fbReadStats.load_all_from_json")
    def test_store_data_to_json_for_year(self, mock_load, mock_json, mock_open):
        mock_load.return_value = {}
        myMock = mock.Mock()
        myMock.dump_to_json.return_value = "test returned dump"
        inputs = {"fake team": myMock}
        store_data_to_json_for_year(2100, inputs)
        self.assertEqual(mock_json.call_args[0][0], {"2100":{"fake team":"test returned dump"}})


    @mock.patch("makostats.fbReadStats.load_from_json")
    def test_load_all_teams_for_year(self, mock_load):
        mock_load.side_effect = [{"fake team": "fake data"}, Exception]
        self.assertEqual({"1776": {"fake team": "fake data"}}, load_all_teams_for_year("1776"))

    @mock.patch("makostats.fbReadStats.json.loads")
    @mock.patch("makostats.fbReadStats.Team.load_from_json")
    def test_load_all_from_json(self, mock_team_load, mock_loads):
        mock_team_load.return_value = mock.Mock()
        returned_data = '{"2008":{"faketeam": "fakedata"},"2009":{},"2010":{},"2011":{},"2012":{},"2013":{},"2014":{},"2015":{},"2016":{},"2017":{}, "2018":{}'

        with mock.patch("makostats.fbReadStats.open", mock.mock_open(read_data=returned_data)) as mock_open:
             with mock.patch("makostats.fbReadStats.json.load") as mock_json:
                mock_json.return_value = {"2008":{"faketeam":"fakedata"},"2009":{},"2010":{},"2011":{},"2012":{},"2013":{},"2014":{},"2015":{},"2016":{},"2017":{}, "2018":{}}
                results = load_all_from_json()
                logging.info(results)
                self.assertTrue(mock_json.called)
                self.assertIsInstance(results, dict)
                self.assertTrue(mock_open.called)
                self.assertEqual(sorted(results.keys()), [str(year) for year in YEARS])
                self.assertEqual(results["2008"]["faketeam"], mock_team_load.return_value)

        with mock.patch("makostats.fbReadStats.open", mock.mock_open(read_data="")) as mock_open:
            mock_open.side_effect = Exception
            results = load_all_from_json()
            self.assertEqual(results, {})

    @mock.patch("makostats.fbReadStats.load_all_from_json")
    def test_load_from_json(self, mock_load ):
        mock_load.return_value = {"2012": {"fake alabama": {"fake attr": 12}}}
        results = load_from_json(2012)
        self.assertEqual({"fake alabama": {"fake attr": 12}}, results)


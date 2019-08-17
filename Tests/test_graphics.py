from unittest import TestCase
from makostats.graphics import MakoPlot, TeamsArray
import mock

class TestTeamsArray(TestCase):

    def setUp(self):
        self.TArray = TeamsArray()
        self.mock_team1 = mock.Mock(team="Team A", year=2012, Total_Games=12.0)
        self.mock_team2 = mock.Mock(team="Team A", year=2013, Total_Games=1.0)
        self.mock_team3 = mock.Mock(team="Team A", year=2014, Total_Games=1.0)
        self.mock_team4 = mock.Mock(team="Team B", year=2014, Total_Games=1.0)


    def test_add_team(self):
        self.TArray.add_team(self.mock_team1)
        self.TArray.add_team(self.mock_team3)
        self.TArray.add_team(self.mock_team2)

        expected_result = {
                            "Team A": [self.mock_team1, self.mock_team2, self.mock_team3]
                            }
        self.assertEqual(expected_result, self.TArray.Teams)


    def test_load_teams(self):
        teams = [self.mock_team1, self.mock_team2, self.mock_team3, self.mock_team4, ]
        expected_result = {
            "Team A": [self.mock_team1, self.mock_team2, self.mock_team3],
            "Team B": [self.mock_team4,],
        }
        new_array = TeamsArray.load_teams(teams)
        self.assertEqual(expected_result, new_array.Teams)


class TestMakoPlot(TestCase):

    def setUp(self):
        self.mock_team1 = mock.Mock(team="Team A", year=2012, Total_Games=12.0, fake=100)
        self.mock_team2 = mock.Mock(team="Team A", year=2013, Total_Games=1.0, fake=200)
        self.mock_team3 = mock.Mock(team="Team A", year=2014, Total_Games=1.0, fake=300)
        self.mock_team4 = mock.Mock(team="Team B", year=2014, Total_Games=1.0, fake=250)
        teams = [self.mock_team1, self.mock_team2, self.mock_team3, self.mock_team4, ]
        self.Plot1 = MakoPlot(teams=teams, attributes=["fake"])
        self.Plot2 = MakoPlot(teams=teams[:-1], attributes=[lambda x: x.fake])

    @mock.patch("makostats.graphics.plt.show")
    @mock.patch("makostats.graphics.plt.legend")
    @mock.patch("makostats.graphics.plt.plot")
    def test_plot(self, mock_plot, mock_legend, mock_show):
        self.Plot1.plot()
        self.assertIn(mock_plot.call_args[1]["label"], ("Team A", "Team B"))
        self.assertTrue(mock_legend.called)
        self.assertTrue(mock_show.called)
        mock_plot.reset_mock()
        mock_legend.reset_mock()
        mock_show.reset_mock()

        self.Plot2.plot()
        self.assertEqual(mock_plot.call_args[0][0], [201212.0, 201301.0, 201401.0])
        self.assertEqual(mock_plot.call_args[0][1], [100, 200, 300])

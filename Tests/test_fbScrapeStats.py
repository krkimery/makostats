from unittest import TestCase
import mock
from fbScrapeStats import get_html_for_team, get_team_name
from fbConsts import TEAMS


class FbScrapeStatsTests(TestCase):

    @mock.patch("fbScrapeStats.requests.get")
    def test_get_html_for_team(self, mock_get):
        mock_resp = mock.Mock()
        mock_resp.text = "mocked html"
        mock_get.return_value = mock_resp
        result = get_html_for_team("Texas Longhorns", 2018)
        self.assertTrue(mock_get.called)
        self.assertEqual("mocked html", result)

    @mock.patch("fbScrapeStats.time.sleep")
    @mock.patch("fbScrapeStats.BeautifulSoup")
    @mock.patch("fbScrapeStats.requests.get")
    def test_get_team_name(self, mock_get, mock_soup, mock_sleep):
        mock_resp = mock.Mock()
        mock_get.return_value = mock_resp
        mock_soup_obj = mock.Mock()
        mock_soup_obj.title.string = "random html gibberish 2012 Delaware Warriors"
        mock_soup.return_value = mock_soup_obj
        result = get_team_name(2012)
        self.assertTrue(mock_get.called)
        self.assertTrue(mock_soup.called)
        self.assertEqual(len(TEAMS), len(result))

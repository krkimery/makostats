from unittest import TestCase
from fbConsts import DATA


class ConstsTests(TestCase):

    def test_DATA(self):
        valid_conferences = ["B12", "B10", "ACC", "PAC12", "SEC", "Other"]
        for team in DATA.keys():
            self.assertIn(DATA[team].get("Conference", "Other"), valid_conferences)
            self.assertIsInstance(DATA[team]["URL"], int)

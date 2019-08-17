from unittest import TestCase
from makostats.fbConsts import DATA, JSON_FILE
import os


class ConstsTests(TestCase):

    def test_DATA(self):
        valid_conferences = ["B12", "B10", "ACC", "PAC12", "SEC", "Other"]
        for team in DATA.keys():
            self.assertIn(DATA[team].get("Conference", "Other"), valid_conferences)
            self.assertIsInstance(DATA[team]["URL"], int)

    def test_json_file_exists(self):
        parent_directory = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(parent_directory, "makostats/"+JSON_FILE)) as f:
            self.assertIsNotNone(f)

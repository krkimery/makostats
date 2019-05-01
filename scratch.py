"""
    Scratch file for testing code snippets for usage in the other modules
"""

from fbScrapeStats import get_html_for_team
from fbReadStats import Team
from bs4 import BeautifulSoup


def testy():
    return BeautifulSoup(get_html_for_team("Texas Longhorns", 2018), "html.parser")


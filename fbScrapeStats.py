
import requests
from bs4 import BeautifulSoup
import time
from fbConsts import DATA, BASE_URL, URL_LIST, HTTP_HEADERS
import logging

logging.getLogger().setLevel(logging.INFO)


def get_team_name(year):
    """Use BeautifulSoup and requests to get a mapping of arbitrary url numbers to team names"""
    team_names = []
    for url in URL_LIST:
        query_url = BASE_URL.format(**{"NUMBER": url, "YEAR": year})
        resp = requests.get(query_url, headers=HTTP_HEADERS)
        soup = BeautifulSoup(resp.text, "html.parser")
        name = soup.title.string.split(str(year)+" ")[-1]
        team_names.append(name)
        logging.info("Added team:{}".format(name))
        time.sleep(3)

    return zip(URL_LIST, team_names)

def get_all_html(year):
    """Retrieve the html text for every team"""
    html = []
    for url in URL_LIST:
        query_url = BASE_URL.format(**{"NUMBER": url, "YEAR": year})
        resp = requests.get(query_url, headers=HTTP_HEADERS)
        time.sleep(3)
        logging.info("Retrieved HTML for {}".format(url))
        html.append(resp.text)
    return html

def get_html_for_team(team, year):
    """GET the specific html text for a team/year"""
    url_int = DATA[team]["URL"]
    query_url = BASE_URL.format(**{"YEAR":year, "NUMBER":url_int})
    logging.info("Scraping for {YEAR} {TEAM}".format(**{"YEAR":year, "TEAM":team}))
    resp = requests.get(query_url, headers=HTTP_HEADERS)
    return resp.text




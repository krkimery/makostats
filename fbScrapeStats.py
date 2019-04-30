
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






















"""



def main():

    #link = ""
    #counter = 0
    #while link == "":
        #try:
            #link = urllib.request.urlopen("http://www.cfbstats.com/2015/team/703/index.html")
        #except:
            #link = ""
            #counter = counter + 1
            #print(counter)
    #textFile = str(link.read())
    

    

    year = "2017"

    #teamName = getTeamName(textFile,year)
    #print(teamName)
    #newFile = open(""+teamName+".txt", "w")
    #newFile.write(textFile)
    #newFile.close()
    urlNumList = [721, 5, 8, 27, 29, 28, 31, 30, 725, 37, 77, 47, 51, 66, 67, 71, 86, 107, 129, 458, 140, 147, 157, 156, 164, 193, 196, 204, 235, 229, 231, 234, 96, 257, 253, 254, 255, 277, 288, 295, 301, 306, 312, 311, 328, 327, 331, 334, 365, 366, 671, 498, 367, 388, 392, 400, 404, 415, 414, 418, 416, 419, 428, 433, 430, 434, 726, 463, 466, 473, 472, 457, 490, 497, 503, 509, 513, 519, 518, 522, 521, 523, 529, 528, 539, 545, 559, 574, 587, 663, 626, 630, 646, 648, 651, 664, 674, 688, 698, 690, 694, 703, 697, 670, 700, 709, 716, 718, 719, 128, 110, 465, 657, 704, 706, 732, 731, 736, 746, 742, 749, 756, 754, 768, 772, 774, 796, 811]
    failures =[]
    try:
        os.chdir("/home/kyle/Desktop/Football Team HTML files/"+year )
    except:
        os.chdir("C:/Users/Kyle/Desktop/Football Team HTML files/"+year )
    for i in urlNumList:
        link = ""
        counter = 0
        while link =="":   
            try:
                link = urllib.request.urlopen("http://www.cfbstats.com/"+year+"/team/"+str(i)+"/index.html", timeout=60)
            except:
                link = ""
                counter += 1
                if counter>0:
                    print(str(i), " failed.")
                    link = "failure"
                    failures.append(i)
                
        if link != "failure":
            textFile = str(link.read())
            teamName = getTeamName(textFile,year)
            print(teamName)
            if teamName != "bad page":
                newFile = open(""+teamName+".txt", "w")
                newFile.write(textFile)
                newFile.close()
    newfailures=[]
    for i in failures:
        link = ""
        counter = 0
        while link =="":   
            try:
                link = urllib.request.urlopen("http://www.cfbstats.com/"+year+"/team/"+str(i)+"/index.html", timeout=30)
            except:
                link = ""
                counter += 1
                if counter>2:
                    print(str(i), " failed. again.")
                    link = "failure"
                    newfailures.append(i)
                
        if link != "failure":
            textFile = str(link.read())
            teamName = getTeamName(textFile,year)
            print(teamName)
            if teamName != "bad page":
                newFile = open(""+teamName+".txt", "w")
                newFile.write(textFile)
                newFile.close()


    for i in newfailures:
        link = ""
        counter = 0
        while link =="":   
            try:
                link = urllib.request.urlopen("http://www.cfbstats.com/"+year+"/team/"+str(i)+"/index.html", timeout=60)
            except:
                link = ""
                counter += 1
                if counter>1:
                    print(str(i), " failed. again.")
                    link = "failure"
                    
                
        if link != "failure":
            textFile = str(link.read())
            teamName = getTeamName(textFile,year)
            print(teamName)
            if teamName != "bad page":
                newFile = open(""+teamName+".txt", "w")
                newFile.write(textFile)
                newFile.close()
"""


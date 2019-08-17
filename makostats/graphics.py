import matplotlib.pyplot as plt
import itertools


class MakoPlot(object):
    """
        Initialize a MakoPlot with a list of Team objects across different time scales

            x-axis is determined by the "Time" of each team object

                    eg:
                        2017Bama, 2016Bama, 2015Bama, 2014Bama, ...

                            axis is 2014, 2015, 2016, 2017

                    eg:

                        2019Bama_week1, 2019Bama_week2, 2019Bama_week3, 2019Bama_week4

                            axis is 2019-1, 2019-2, 2019-3, 2019-4


            y-axis is determined by the value of the passed in attr for each of the team objects
                ALTERNATIVELY, you can pass a function which acts on team objects

                    eg:
                        "passingYardsPerGame" : 2017Bama - 256.2, 2016Bama - 194.3, 2015Bama - 214.7

                            axis is passing yards per game... 0 - 256.2

                    MakoPlot is set with alabama 2015-2017, with the attr "passingYardsPerGame", so the
                    plot object reads the value of the passing yardage attribute on each of the passed in
                    team objects.


            Other thoughts:

                -pass in a list of attributes for Y, instead of just a single attribute. Then normalize each of
                 the resulting y-axis plots, so that you can compare teams across several attributes?

    """



    def __init__(self, teams, attributes):
        self.symbols = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "s", "p", "*", "h", "H", "+", "x", "D", "d","|"]
        self.colors = ["b-", "g-", "r-", "c-", "m-", "y-", "k-",]
        self.teams = teams
        self.attributes = attributes
        self.Teams_Array = TeamsArray.load_teams(self.teams)

    def plot(self):
        formats = itertools.product(self.symbols, self.colors)
        if len(self.attributes)>1:
            raise NotImplementedError("oops - I haven't done this yet..")
        for attribute in self.attributes:
            for team_name in self.Teams_Array.Teams:
                format_type = "".join(next(formats))
                x_vals = []
                y_vals = []
                for team_obj in self.Teams_Array.Teams[team_name]:
                    x_vals.append(100 * team_obj.year + team_obj.Total_Games)
                    if isinstance(attribute, basestring):
                        y_vals.append(float(getattr(team_obj, attribute)))
                    else:
                        y_vals.append(attribute(team_obj))
                plt.plot(x_vals, y_vals, format_type, label=team_name)
        plt.legend()
        plt.show()





class TeamsArray(object):

    def __init__(self):
        self.Teams = {}
        self._axis = set()

    def add_team(self, new_team_object):
        team_data = self.Teams.setdefault(new_team_object.team, [])
        team_data.append(new_team_object)
        self._axis.add(int(100 * new_team_object.year + new_team_object.Total_Games))
        self.Teams[new_team_object.team] = sorted(team_data, key=lambda tm: 100*tm.year+tm.Total_Games)

    @classmethod
    def load_teams(cls, teams_list):
        new_teams_array = TeamsArray()
        for team in teams_list:
            new_teams_array.add_team(team)
        return new_teams_array




'''
#SAMPLE

import makostats.fbReadStats
teams = makostats.fbReadStats.load_all_from_json()
bama = []
for year in teams:
    for name in teams[year]:
        if str(name) in ["Arkansas Razorbacks", "Texas Longhorns", "Texas A&M Aggies", ]:
            bama.append(teams[year][name])
            
import makostats.algos
import makostats.graphics
plot = makostats.graphics.MakoPlot(bama, [makostats.algos.mako])
plot.plot()

'''
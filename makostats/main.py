"""

	Main: rank teams based off of various ranking algorithms


"""
import logging
import makostats.algos
import makostats.fbReadStats
from makostats.fbConsts import AP_RANKING, DATA
import makostats.graphics


def display_rankings(all_rankings_teams):
	"""
		Display the results of the ranking algo alongside the AP Rank
		Given:
			all_rankings_dict	(dict)	dict of the ordered teams for the years
		Return:
			None - log results to console
	"""
	plot = makostats.graphics.MakoPlot(all_rankings_teams, [makostats.algos.mako])
	plot.plot()


def get_all_teams(all_years_dict):
	"""
		Apply the ranking algorithm(s) to the team objects
		Given:
			all_years_dict	(dict)	dict of team objects and years
		Return:
			(dict) results of ranking algorithm
	"""
	all_teams = []
	in_scope_teams = [
						"Alabama Crimson Tide",
						"Clemson Tigers",
						"Texas Longhorns",
						"Texas A&M Aggies",
						"Arkansas Razorbacks",
						"Florida Gators",
						"Florida State Seminoles",
						"Oregon Ducks",
	]

	Big10 = [team for team in DATA if DATA[team].get("Conference", None) == "B10"]
	Acc = [team for team in DATA if DATA[team].get("Conference", None) == "ACC"]
	Pac12 = [team for team in DATA if DATA[team].get("Conference", None) == "PAC12"]
	Sec = [team for team in DATA if DATA[team].get("Conference", None) == "SEC"]
	Big12 = [team for team in DATA if DATA[team].get("Conference", None) == "B12"]

	ap2018 = AP_RANKING[2018]
	ap2017 = AP_RANKING[2017]
	ap2016 = AP_RANKING[2016]
	ap2015 = AP_RANKING[2015]
	ap2014 = AP_RANKING[2014]
	ap2013 = AP_RANKING[2013]
	ap2012 = AP_RANKING[2012]
	ap2011 = AP_RANKING[2011]
	ap2010 = AP_RANKING[2010]
	ap2009 = AP_RANKING[2009]
	ap2008 = AP_RANKING[2008]

	in_scope_teams = ap2018

	for year, team_dict in all_years_dict.iteritems():
		logging.info("Filtering teams for year: {}".format(year))
		for team, team_obj in all_years_dict[year].iteritems():
			if team in in_scope_teams:
				all_teams.append(team_obj)

	return all_teams

if __name__ == "__main__":
	logging.info("Building all teams")
	all_years_dict = makostats.fbReadStats.build_all_teams()
	all_rankings_teams = get_all_teams(all_years_dict)
	display_rankings(all_rankings_teams)



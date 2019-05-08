"""

	Main: rank teams based off of various ranking algorithms


"""
import logging
import algos
import fbReadStats
from fbConsts import AP_RANKING





if __name__ =="__main__":
	logging.info("Building all teams")
	all_years_dict = fbReadStats.build_all_teams()
	all_rankings_dict = {}
	for year, team_dict in all_years_dict.iteritems():
		all_rankings_dict[year] = []
		logging.info("Ranking teams for year: {}".format(year))
		for team, team_obj in all_years_dict[year].iteritems():
			try:
				team_obj.mako = algos.mako(team_obj)
				all_rankings_dict[year].append(team_obj)
			except:
				logging.warn("Failed to rank team: {} {}".format(year, team))
				continue

	for year, results in all_rankings_dict.iteritems():
		logging.info("Rankings for year: {}".format(year))
		ranked = sorted(results, key=lambda obj:obj.mako)[:30:-1]
		logging.info("{}".format([res.team for res in ranked]))
		logging.info("{}".format(AP_RANKING.get(year)))
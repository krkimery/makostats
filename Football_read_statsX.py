

import os, re



class Team:



	def __init__(self):
	
	
	

		self.team = None						#complete!				#team name, string
		self.conference = None					#complete, mostly		#conference the team is in
		
		self.mako = None					#ranking algorithm, mostly equal weight given to yardage/scoring as well as winrates and adjusted for strength of schedule
		
		self.ajax = None
		
		
		#************************************	RECORD AND SCORING	 ***************************************************************
		
		self.record = ""						#complete!				#win-loss record, string
		self.wins = None						#complete!				#total wins, int
		self.losses = None						#complete!				#total losses, int
		self.winrate = None						#complete!				#wins/(wins+losses), float
		
		self.fbsGoodRecord = ""					#complete!				#record vs fbs teams with winning records
		self.fbsGoodWins = None					#complete!				#wins vs fbs teams with winning records
		self.fbsGoodLosses = None				#complete!				#losses vs fbs teams with winning records
		self.fbsGoodWinrate = None				#complete!				#winrate vs fbs teams with winning records
		
		self.fbsBadRecord = ""					#complete!				#record vs fbs teams with winning records
		self.fbsBadWins = None					#complete!				#wins vs fbs teams with winning records
		self.fbsBadLosses = None				#complete!				#losses vs fbs teams with winning records
		self.fbsBadWinrate = None				#complete!				#winrate vs fbs teams with winning records
		
		self.fcsRecord = ""						#complete!				#record vs fcs teams
		self.fcsWins = None						#complete!				#wins vs fcs teams
		self.fcsLosses = None					#complete!				#losses vs fcs teams
		self.fcsWinrate = None					#complete!				#winrate vs fcs teams
		
		self.pFiveRecord = ""					#complete!				#record vs power 5 teams
		self.pFiveWins = None					#complete!				#wins vs power 5 teams
		self.pFiveLosses = None					#complete!				#losses vs power 5 teams
		self.pFiveWinrate = None				#complete!				#winrate vs power 5 teams
		
		
		self.pointsPerGameScored = None			#complete!				#points scored per game, float
		self.pointsPerGameAllowed = None		#complete!				#points allowed per game, float
		self.pointsPerGameDiffRaw = None		#complete!				#point differntial between teams, float
		self.pointsPerGameDiffPerc = None		#complete!				#point ratio between teams, float
		
		
		
		
		
		#************************************	OFFENSIVE RUSHING	*****************************************************************
		
		self.rushYards = None					#complete!				#total rushing yards on the season as a whole, int
		self.rushYardsPerGame = None			#complete!				#rushing yards per game
		self.rushAttempts = None				#complete!				#rushing play attempts
		self.rushYardsPerAttempt = None			#complete!				#rushing yards per attempt
		self.fumbles = None
		
		
		
		
		#************************************	DEFENSIVE RUSHING	*****************************************************************
		
		self.rushYardsAllowed = None			#complete!				#number of rushing yads by enemies
		self.rushAttemptsAllowed = None			#complete!				#number of rushing attempts by enemies
		self.rushYardsPerGameAllowed = None		#complete!				#number of rushing yards per game by enemies
		self.rushYardsPerAttemptAllowed = None	#complete!				#number of rushing yards per attempt by enemies
		self.forcedFumbles = None
		
		
		
		
		#************************************	OFFENSIVE PASSING	********************************************************************
		
		self.passYards = None					#complete!				#passing yards total by team
		self.passYardsPerGame = None			#complete!				#pass yards per game by team
		self.passAttempts = None				#complete!				#pass attempts by the offense
		self.passCompletions = None				#complete!				#passes completed by the offense
		self.passYardsPerAttempt = None			#complete!				#passing yards per attempted pass
		self.passerRating = None
		self.passTDThrown = None				#complete!				#TD passes thrown by the offense
		self.passTDCaughtPerIntThrown = None	#complete!				#ratio of TD pass thrown by the offense to their interceptions
		self.intThrown = None					#complete!				#interceptions thrown by the offense
		self.passTDThrownPerAttempt = None		#complete!				#TD passes thrown by the offense compared to the pass attempts
		self.intThrownPerAttempt = None			#complete!				#interceptions thrown per pass attempt by the offense
		
		
		
		
		#************************************	DEFENSIVE PASSING	*****************************************************************
		
		self.passYardsAllowed = None			#complete!				#passing yards allowed by the defense			  
		self.passAttemptsAllowed = None			#complete!				#pass attempts against the defense
		self.passCompletionsAllowed = None		#complete!				#pass completions allowed by the defense
		self.passYardsPerAttemptAllowed = None	#complete!				#passing yards allowed by the defense per pass attempt
		self.passYardsPerGameAllowed = None		#complete!				#passing yards allowed by the defense per game
		self.passerRatingAllowed = None
		self.passTDAllowed = None				#complete!				#passing TDs allowed by the defense
		self.intCaught = None					#complete!				#interceptions caught by the defense
		self.passTDAllowedPerIntCaught = None	#complete!				#passing TDs allowed by the defense per interception caught
		self.passTDAllowedPerAttempt = None		#complete!				#passing TDs allowed by the defense per pass attempt
		self.intCaughtPerAttempt = None			#complete!				#interceptions caught by the defense per pass attempt
		
		
		
		
		#************************************	OFFENSIVE AND DEFENSIVE SPECIAL TEAMS	***************************************************
		
		self.puntReturnYards = None
		self.puntReturnYardsAllowed = None
		self.kickReturnYards = None
		self.kickReturnYardsAllowed = None
		self.fieldGoalPercent = None
		
		
		
		
		#************************************	EFFICIENCY	 *****************************************************************************
		
		self.time = None
		self.thirdDownConv = None
		self.thirdDownConvAllowed = None
		self.fourthDownConv = None
		self.fourthDownConvAllowed = None
		self.redZoneVisits = None
		self.redZoneVisitsAllowed = None
		self.redZonePercent = None
		self.redZonePercentAllowed = None
		
		
			
						
	def __str__(self):																			
		return str(self.team)																	
																								
	







	
																								
def getStats(team, file,stats, year):

	stattext = open(file, "r")
	
	team.team = file[:-4]										#this assigns the teamname based on the file name
	stats=stats+team.team+"\t"
	
	
	
	
	#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     CONFERENCES     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	#
	#									These lists represent the P5 conferences as of pre-season 2016 (8/18/2016)
	#
	#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	
	
	
	SEC = ["Alabama Crimson Tide", "Arkansas Razorbacks", "Auburn Tigers", "LSU Tigers", "Mississippi State Bulldogs", "Mississippi Rebels", "Texas A&M Aggies", "Florida Gators", "Georgia Bulldogs", "Kentucky Wildcats", "Missouri Tigers", "South Carolina Gamecocks", "Tennessee Volunteers", "Vanderbilt Commodores"]
	PAC12 = ["California Golden Bears", "Oregon Ducks", "Oregon State Beavers", "Stanford Cardinal", "Washington Huskies", "Washington State Cougars", "Arizona State Sun Devils", "Arizona Wildcats", "Colorado Buffaloes", "UCLA Bruins", "USC Trojans", "Utah Utes"]
	B10 = ["Illinois Fighting Illini", "Maryland Terrapins", "Michigan State Spartans", "Michigan Wolverines", "Ohio State Buckeyes", "Penn State Nittany Lions", "Rutgers Scarlet Knights", "Indiana Hoosiers", "Iowa Hawkeyes", "Minnesota Golden Gophers", "Nebraska Cornhuskers", "Northwestern Wildcats", "Purdue Boilermakers", "Wisconsin Badgers"]
	B1G = B10
	ACC = ["Boston College Eagles", "Clemson Tigers", "Florida State Seminoles", "Louisville Cardinals", "North Carolina State Wolfpack", "Syracuse Orange", "Wake Forest Demon Deacons", "Duke Blue Devils", "Georgia Tech Yellow Jackets", "Miami (Florida) Hurricanes", "North Carolina Tar Heels", "Pittsburgh Panthers", "Virginia Cavaliers", "Virginia Tech Hokies"]
	BIG12 = ["Baylor Bears", "Iowa State Cyclones", "Kansas Jayhawks", "Kansas State Wildcats", "Oklahoma Sooners", "Oklahoma State Cowboys", "TCU Horned Frogs", "Texas Longhorns", "Texas Tech Red Raiders", "West Virginia Mountaineers"]
	
	
	
	
	if team.team in BIG12:
		team.conference = "BIG12"
	elif team.team in SEC:
		team.conference = "SEC"
	elif team.team in PAC12:
		team.conference = "PAC12"
	elif team.team in B1G:
		team.conference = "B1G"
	elif team.team in ACC or team.team == "Notre Dame Fighting Irish":
		team.conference = "ACC"
	else:
		team.conference = "Other"
	
	
	
	
	
	
	
	
	
	#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     TOP 25     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	#
	#									These if statements define the list "TOP25" based upon the current year being observed.
	#
	#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	
	
	
	if year=="2015":
		TOP25 = ["Alabama Crimson Tide","Clemson Tigers","Stanford Cardinal","Oklahoma Sooners","Ohio State Buckeyes","Michigan State Spartans","TCU Horned Frogs","Mississippi Rebels", "Notre Dame Fighting Irish", "Michigan Wolverines","Baylor Bears","North Carolina Tar Heels","Florida State Seminoles","Oklahoma State Cowboys","LSU Tigers","Utah Utes","Oregon Ducks","Florida Gators","Tennessee Volunteers","Northwestern Wildcats","USC Trojans","Mississippi State Bulldogs","Georgia Bulldogs"]
	elif year =="2014":
		TOP25 = ["Ohio State Buckeyes","Oregon Ducks","TCU Horned Frogs","Alabama Crimson Tide","Florida State Seminoles","Michigan State Spartans","Baylor Bears","Georgia Tech Yellow Jackets","Georgia Bulldogs","UCLA Bruins","Mississippi State Bulldogs","Arizona State Sun Devils","Wisconsin Badgers","Missouri Tigers","Clemson Tigers","Mississippi Rebels","Kansas State Wildcats","Arizona Wildcats","USC Trojans","Utah Utes","Auburn Tigers","Louisville Cardinals","Notre Dame Fighting Irish","Stanford Cardinal","Nebraska Cornhuskers",]
	elif year == "2013":
		TOP25 = ["Florida State Seminoles","Auburn Tigers","Michigan State Spartans","South Carolina Gamecocks","Missouri Tigers","Oklahoma Sooners","Alabama Crimson Tide","Clemson Tigers","Oregon Ducks","Stanford Cardinal","Ohio State Buckeyes","Baylor Bears","LSU Tigers","Louisville Cardinals","UCLA Bruins","Oklahoma State Cowboys","Texas A&M Aggies","USC Trojans","Notre Dame Fighting Irish","Arizona State Sun Devils","Wisconsin Badgers","Duke Blue Devils","Vanderbilt Commodores","Washington Huskies","Texas Tech Red Raiders",]
	elif year == "2012":
		TOP25 = ["Alabama Crimson Tide","Oregon Ducks","Ohio State Buckeyes","Notre Dame Fighting Irish","Georgia Bulldogs","Texas A&M Aggies","Stanford Cardinal","South Carolina Gamecocks","Florida Gators","Florida State Seminoles","Clemson Tigers","Kansas State Wildcats","Louisville Cardinals","LSU Tigers","Oklahoma Sooners","Northwestern Wildcats","Texas Longhorns","Oregon State Beavers","Vanderbilt Commodores","Michigan Wolverines","Nebraska Cornhuskers","Baylor Bears","Penn State Nittany Lions","Oklahoma State Cowboys","UCLA Bruins",]
	elif year == "2011":
		TOP25 = ["Alabama Crimson Tide","LSU Tigers","Oklahoma State Cowboys","Oregon Ducks","Arkansas Razorbacks","USC Trojans","Stanford Cardinal","South Carolina Gamecocks","Wisconsin Badgers","Michigan State Spartans","Michigan Wolverines","Baylor Bears","TCU Horned Frogs","Kansas State Wildcats","Oklahoma Sooners","West Virginia Mountaineers","Georgia Bulldogs","Virginia Tech Hokies","Clemson Tigers","Florida State Seminoles","Nebraska Cornhuskers","Auburn Tigers","Missouri Tigers","Texas Longhorns","Rutgers Crimson Knights",]
	elif year == "2010":
		TOP25 = ["Auburn Tigers","TCU Horned Frogs","Oregon Ducks","Stanford Cardinal","Ohio State Buckeyes","Oklahoma Sooners","Wisconsin Badgers","LSU Tigers","Alabama Crimson Tide","Arkansas Razorbacks","Oklahoma State Cowboys","Michigan State Spartans","Mississippi State Bulldogs","Virginia Tech Hokies","Florida State Seminoles","Missouri Tigers","Texas A&M Aggies","Nebraska Cornhuskers","South Carolina Gamecocks","Maryland Terrapins","North Carolina State Wolfpack","Utah Utes","West Virginia Mountaineers","Arizona Wildcats","Iowa Hawkeyes",]
	elif year == "2009":
		TOP25 = ["Florida Gators","Texas Longhorns","Oklahoma Sooners","USC Trojans","Alabama Crimson Tide","Ohio State Buckeyes","Virginia Tech Hokies","Mississippi Rebels","Oklahoma State Cowboys","Penn State Nittany Lions","LSU Tigers","California Golden Bears","Georgia Bulldogs","Georgia Tech Yellow Jackets","Oregon Ducks","TCU Horned Frogs","Florida State Seminoles","Utah Utes","North Carolina Tar Heels","Iowa Hawkeyes","Notre Dame Fighting Irish","Nebraska Cornhuskers","Kansas Jayhawks","Texas Tech Red Raiders","Oregon State Beavers",]
	elif year == "2008":
		TOP25 = ["Florida Gators","Utah Utes","USC Trojans","Texas Longhorns","Oklahoma Sooners","Alabama Crimson Tide","TCU Horned Frogs","Penn State Nittany Lions","Ohio State Buckeyes","Oregon Ducks","Texas Tech Red Raiders","Georgia Bulldogs","Mississippi Rebels","Virginia Tech Hokies","Oklahoma State Cowboys","Oregon State Beavers","Missouri Tigers","Iowa Hawkeyes","Florida State Seminoles","Georgia Tech Yellow Jackets","West Virginia Mountaineers","Michigan State Spartans","Northwestern Wildcats","Pittsburgh Panthers","Iowa Hawkeyes",]
	else:
		TOP25 = []
		
		
		
		
		
		
		
		
		
		
		
	
	
	#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     READ STATS FROM FILE     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	#
	#									The next bulk of code reads the stats from the HTML file to store as variables in each team object.
	#
	#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	
	
	

	regex = r'(All Games</td>\\r\\n    <td>)(\d+)(.)(\d+)'   
	match = re.search(regex, stattext.read().replace('\n', ''))
	#print("Wins: %s" % (match.group(2)))
	#print("Losses: %s" % (match.group(4)))
	
	
	team.wins = int(match.group(2))											#determines the teams win total
	team.losses = int(match.group(4))										#determines the teams loss total
	
	if team.losses==0:
		team.winrate = 1.0
	else: team.winrate = float(team.wins)/(team.wins+team.losses)



	
	
	stattext = open(file, "r")
	regex = r'(>vs. FBS Winning</td>\\r\\n    <td>)(\d+)(.)(\d+)'   
	match = re.search(regex, stattext.read().replace('\n', ''))
	#print("Wins: %s" % (match.group(2)))
	#print("Losses: %s" % (match.group(4)))
	


	team.fbsGoodWins = int(match.group(2))			
	team.fbsGoodLosses = int(match.group(4))		

	if team.fbsGoodLosses==0:
		team.fbsGoodWinrate = 1.0
	else: team.fbsGoodWinrate = float(team.fbsGoodWins)/(team.fbsGoodWins+team.fbsGoodLosses)
	
	
	

	stattext = open(file, "r")
	regex = r'(>vs. FBS Non-Winning</td>\\r\\n    <td>)(\d+)(.)(\d+)'   
	match = re.search(regex, stattext.read().replace('\n', ''))
	#print("Wins: %s" % (match.group(2)))
	#print("Losses: %s" % (match.group(4)))
			
	team.fbsBadWins = int(match.group(2))			
	team.fbsBadLosses = int(match.group(4))		

	if team.fbsBadLosses==0:
		team.fbsBadWinrate = 1.0
	else: team.fbsBadWinrate = float(team.fbsBadWins)/(team.fbsBadWins+team.fbsBadLosses)
	
	
	
	stattext = open(file, "r")
	regex = r'(vs. FCS \(I-AA\)</td>\\r\\n    <td>)(\d+)(.)(\d+)'   
	match = re.search(regex, stattext.read().replace('\n', ''))
	#print("Wins: %s" % (match.group(2)))
	#print("Losses: %s" % (match.group(4)))
		
	team.fcsWins = int(match.group(2))			
	team.fcsLosses = int(match.group(4))		

	if team.fcsLosses==0:
		team.fcsWinrate = 1.0
	else: team.fcsWinrate = float(team.fcsWins)/(team.fcsWins+team.fcsLosses)
	
	
	
	stattext = open(file, "r")
	regex = r'(>vs. FBS Power 5</td>\\r\\n    <td>)(\d+)(.)(\d+)'   
	match = re.search(regex, stattext.read().replace('\n', ''))
	#print("Wins: %s" % (match.group(2)))
	#print("Losses: %s" % (match.group(4)))
	team.pFiveWins = int(match.group(2))			
	team.pFiveLosses = int(match.group(4))		

	if team.pFiveLosses==0:
		team.pFiveWinrate = 1.0
	else: team.pFiveWinrate = float(team.pFiveWins)/(team.pFiveWins+team.pFiveLosses)
	
	
	
	
	
	#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     SAMPLE CODE PARSE     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$	
	#	
	#							This is a sample piece of code for parsing the HTML text for the desired stat. 
	#	
	#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

	
	#count = 0
	#stattext = open(file, "r")
	
	#for line in stattext:
		#for i in range(len(line)):													#***************************************************************************************
			#if i>=9 and line[i-9:i]=="All Games" and team.record=="":				 #THE NUMBER (9 IN THIS CASE) IS THE SAME AS THE LENGTH OF THE KEY PHRASE ("ALL GAMES") aka: all the text between the < and >
				#for j in range(i+17, len(line)):									#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
					
					#if line[j]=="<":
						#team.record = line[i+17:i+17+count]
						#break
					
					#count = count + 1

 
 
 
 
 
 
 
 
 
 
	count = 0
	count2 = 0
	stattext = open(file, "r")
	
	regex = r'(Points/Game</td>\\r\\n    <td>)(\d+.\d+)(</td>\\r\\n    <td>)(\d+.\d+)'   
	match = re.search(regex, stattext.read().replace('\n', ''))
	
	try:
		team.pointsPerGameScored = float(match.group(2))
	except ValueError:
		team.pointsPerGameScored = -1
					
	try:
		team.pointsPerGameAllowed = float(match.group(4))		   	#The number is a float, determined by 2 "counts" the counts determine the length of the strings
	except ValueError:
		team.pointsPerGameAllowed = -1
	if team.pointsPerGameAllowed < 1:
		team.pointsPerGameAllowed = 1
					
	

	team.pointsPerGameDiffRaw = team.pointsPerGameScored - team.pointsPerGameAllowed							#This code determines the 2 stats: pointsPerGameDiffRaw and pointsPerGameDiffPerc
	if team.pointsPerGameAllowed > 1.0:
		team.pointsPerGameDiffPerc = team.pointsPerGameScored/team.pointsPerGameAllowed
	else:
		team.pointsPerGameDiffPerc = team.pointsPerGameScored



	count = 0
	stattext = open(file, "r")
	regex = r'(Rushing:  Attempts - Yards - TD</td>\\r\\n    <td>)(\d+) . (\d+) . (\d+)(</td>\\r\\n    <td>)(\d+) . (\d+) . (\d+)'   
	match = re.search(regex, stattext.read().replace('\n', ''))											   

	team.rushAttempts = int(match.group(2))															#-1 because of a space in the string that needs to be ignored
	team.rushYards = int(match.group(3))						#countFromDash - 1 because we don't want the "-" in the variable
						


	if team.wins +team.losses != 0:
		team.rushYardsPerGame = float(team.rushYards/(team.wins+team.losses))
	else:
		team.rushYardsPerGame = 0
	if team.rushAttempts != 0:
		team.rushYardsPerAttempt = float(team.rushYards/team.rushAttempts)
	else:
		team.rushYardsPerAttempt = 0



	team.rushAttemptsAllowed = int(match.group(6))										#code determines the rush attempts per game against the team
	team.rushYardsAllowed = int(match.group(7))
								
				   
		
	if team.wins +team.losses != 0:																				#code determines per game averages of rushing stats for and against the team
		team.rushYardsPerGameAllowed = float(team.rushYardsAllowed/(team.wins+team.losses))
	else:
		team.rushYardsPerGameAllowed = -1
	if team.rushAttemptsAllowed != 0:
		team.rushYardsPerAttemptAllowed = float(team.rushYardsAllowed/team.rushAttemptsAllowed)
	else:
		team.rushYardsPerAttemptAllowed = 0





	count = 0
	stattext = open(file, "r")
	regex = r'(>Passing:  Yards</td>\\r\\n    <td>)(\d+)(</td>\\r\\n    <td>)(\d+)'   
	match = re.search(regex, stattext.read().replace('\n', ''))										   
			
	team.passYards = int(match.group(2))
	team.passYardsAllowed = int(match.group(4))					 
						

	
	if team.wins +team.losses != 0:
		team.passYardsPerGame = float(team.passYards/(team.wins+team.losses))										#per game stats for passing yards
	else:
		team.passYardsPerGame = 0


	count = 0
	startcount=0
	stattext = open(file, "r")
	
	regex = r'(>Passing:  Attempts - Completions - Interceptions - TD</td>\\r\\n    <td>)(\d+) . (\d+) . (\d+) . (\d+)(</td>\\r\\n    <td>)(\d+) . (\d+) . (\d+) . (\d+)'   
	match = re.search(regex, stattext.read().replace('\n', ''))																			

	team.passAttempts = int(match.group(2))
	team.passCompletions = int(match.group(3))
	team.intThrown = int(match.group(4))
	team.passTDThrown = int(match.group(5))							#defensive passing stats: attempts allowed, completions allowed, ints caught, TDs allowed
	team.passAttemptsAllowed = int(match.group(7))
	team.passCompletionsAllowed = int(match.group(8))
	team.intCaught = int(match.group(9))
	team.passTDAllowed = int(match.group(10))
	
	if team.wins + team.losses !=0:
		team.passYardsPerGameAllowed = 1.0*team.passYardsAllowed / (team.wins+team.losses)							#defensive passing yards per game
	else: 
		team.passYardsPerGameAllowed = -1
		
		
		
	if team.passAttempts!=0:
		team.passYardsPerAttempt = 1.0*team.passYards/team.passAttempts												#offensive passing yards per attempt
					
	if team.passAttemptsAllowed!=0:
		team.passYardsPerAttemptAllowed= 1.0*team.passYardsAllowed/team.passAttemptsAllowed
					
	if team.intThrown!=0:
		team.passTDCaughtPerIntThrown=1.0*team.passTDThrown/team.intThrown											#ratio of offensive TDs thrown per int thrown
					
	if team.intCaught!=0:
		team.passTDAllowedPerIntCaught=1.0*team.passTDAllowed/team.intCaught										#ratio of defensive TDs allowed to int caught
					
	if team.passAttempts!=0:
		team.passTDThrownPerAttempt = 1.0*team.passTDThrown/team.passAttempts										#offensive TDs per attempt, int per attempt
		team.intThrownPerAttempt = 1.0*team.intThrown/team.passAttempts
					
	if team.passAttemptsAllowed !=0:
		team.passTDAllowedPerAttempt = 1.0*team.passTDAllowed/team.passAttemptsAllowed								#defensive TDS allowed per attempt, int caught per attempt
		team.intCaughtPerAttempt = 1.0*team.intCaught/team.passAttemptsAllowed

				
	
	
	if (team.fbsGoodWins+team.fbsBadWins+team.fbsGoodLosses+team.fbsBadLosses) == 0:
		team.fbsBadLosses = -1
	
	
	#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&     RANKING ALGORITHMS     &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
	#
	#								This is where the ranking algortihms are computed. Mako is the first algorithm, designed to balance winrate and stats while 
	#								accounting for strength of schedule. The current mako iteration is mako 1.0 (8/18/2016)
	#
	#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
	
	
	
	
	team.mako = (0.6)*(team.rushYardsPerGame/180)+(0.49)*(157/team.rushYardsPerGameAllowed)+(0.47)*(team.passYardsPerGame/238)+(0.46)*(215/team.passYardsPerGameAllowed)+(0.67)*(team.pointsPerGameScored/31)+(0.55)*(25/team.pointsPerGameAllowed)+(0.9)*(team.winrate/.62) -1.3*(1-(team.pFiveWins+team.pFiveLosses)/(team.fbsGoodWins+team.fbsBadWins+team.fbsGoodLosses+team.fbsBadLosses))-(0.5-team.fbsGoodWinrate)-(0.5-team.pFiveWinrate)-(.9-team.fbsBadWinrate)
	
	team.ajax = 1.2*(team.fbsGoodWinrate/0.4)+1.1*(team.pFiveWinrate/0.5)+(0.7)*((team.pointsPerGameScored-team.pointsPerGameAllowed)/7)-1.75*(1-(team.pFiveWins+team.pFiveLosses)/(team.fbsGoodWins+team.fbsBadWins+team.fbsGoodLosses+team.fbsBadLosses))-2.25*(1-team.fbsBadWinrate)
	
	
	
	
	
	#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      EXCEL FORMATTING      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
	#
	#								This is where relevant information is formatted for export to Excel 2010
	#
	#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
	
	
	
	
	
	if team.conference != None: 					#!= "Other" or team.team == "Houston Cougars":
		stats=stats+str(round(team.mako,4))+"\t"+str(round(float(team.ajax), 3))+"\t"+str(round(float(team.rushYardsPerGameAllowed), 2))+"\t"+str(round(float(team.passYardsPerGame), 2))+"\t"+str(round(float(team.passYardsPerGameAllowed), 2))+"\t"+str(round(float(team.pointsPerGameScored), 3))+"\t"+str(round(team.pointsPerGameAllowed, 3))+"\t"+str(round(float(team.winrate), 4))+"\t"+str(round(float(-1.3*(1-(team.pFiveWins+team.pFiveLosses)/(team.fbsGoodWins+team.fbsBadWins+team.fbsGoodLosses+team.fbsBadLosses))), 2))+"\t"+str(round(float(-(0.5-team.fbsGoodWinrate)), 2))+"\t"+str(round(float(-(0.5-team.pFiveWinrate)), 2))+"\t"+str(round(float(-(.9-team.fbsBadWinrate)), 2))+"\t"

	
	
	#******************************************************************       TESTING       *****************************************************************************************************************************************
	#
	#								This is where I test the relationships between stats and overall team success. As well as anything else. 
	#
	#*********************************************************************************************************************************************************************************************************************************
	
	
	#team.fbsGoodWinrate > 0.4  team.pFiveWinrate >0.5 team.pointsPerGameScored-team.pointsPerGameAllowed > 7
	

		
	return [stats,0,0]





























































def main():
	
	
	
	rankweight = 0																				#variable that tracks the number of ranked teams that meet certain criteria
	totalTeams = 0																				#total number of teams that meet that same certain criteria
	
	for j in ["2016"]:						#["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]:
	
		year = j
		print(year)
		
		os.chdir("/Users/Kyle/Desktop/"+year)							#changes the current working directory to the "year" being examined in the for loop
		statfile = open(""+year+" Stats.txt", "w")												#creates a txt file to store the stats in an excel-friendly format
		stats = "TEAM\tmako\tajax\tDr/gm\tOp/gm\tDp/gm\tOpts/gm\tDpts/gm\twinr\t"				#the text that will populate the txt file for the excel file
		
		for i in os.listdir(os.getcwd()):														#for looop that iterates through all the files in the current working directory
			
			if i.endswith(".txt") and not i.startswith("2"):									#this conditional checks if the file being examined is one of the html files for the teams
			
				stats = stats+"\n"
				tempTeam = Team()																#temporary variable for the team in the html file being examined
				tempVar = getStats(tempTeam, i,stats, j)										#this calls the main stat-reading program
				rankweight = rankweight + tempVar[1]
				totalTeams = totalTeams + tempVar[2]
				stats = tempVar[0]
				print(tempTeam.team)
				
				
				
		
		statfile.write(stats)																	#writes the text from "stats" to the excel-friendly file
	#print(rankweight,"/",totalTeams)															#this determines the ratio of ranked teams to total teams in a certain category 		
	 

main()










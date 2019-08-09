'''
    The various ranking algorithms that I've pieced together
'''


def mako(team):
    return (0.6) * (team.Rushing_Yards_Per_Game/180.0) + (0.49)*(157.0/team.Defense_Rushing_Yards_Per_Game) + (0.47) * \
           (team.Passing_Yards_Per_Game/238.0) + (215.0/team.Defense_Passing_Yards_Per_Game) + \
           (0.67)*(team.Scoring_Points_Per_Game/31.0) + (0.55)*(25.0/team.Defense_Scoring_Points_Per_Game) + \
           (0.9)*(team.Winrate/0.62) - \
           (1.3)*(1-(team.Wins_vs_FBS_Power_5 + team.Losses_vs_FBS_Power_5)/
                  (team.Wins_vs_FBS_Winning +
                   team.Wins_vs_FBS_Non_Winning +
                   team.Losses_vs_FBS_Non_Winning +
                   team.Losses_vs_FBS_Winning)) - \
           (0.5 - team.FBS_Winning_Winrate) - (0.5 - team.FBS_Losing_Winrate) - (0.9 - team.Power_5_Winrate)

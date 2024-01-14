import random
def toss_winner(team_1,team_2):
    teams = [team_1, team_2]
    toss_winner = random.choice(teams)
    return toss_winner

def toss_decision():
    decisions = ["bat","ball"]
    toss_decision = random.choice(decisions)
    return toss_decision


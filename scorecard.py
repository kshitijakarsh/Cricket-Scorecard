import toss
import batsman_change
import striker_change
import bowler_runs
import matplotlib.pyplot as plt
import numpy as np

location = input("Location : ")


team_1 = input("Enter Team 1 Name ")
team_1_players = []

for i in range(11):
    players_team_1 = input(f"Enter player names {i} > ")
    team_1_players.append(players_team_1)


team_2 = input("Enter Team 2 Name ")
team_2_players = []
for j in range(11):
    players_team_2 = input(f"Enter player names {j} > ")
    team_2_players.append(players_team_2)



toss_winner = toss.toss_winner(team_1, team_2)
toss_decision = toss.toss_decision()



wickets = 0
over = int(input("Enter number of overs "))  # to enter the number of overs the match is going to be off
balls = over * 6



run = 0
i = 0
over_by_over_run = []
run_over = 0

strike = team_1_players[0]
non_strike = team_1_players[1]
run_ba1 = 0
run_ba2 = 0
run_ba3 = 0
run_ba4 = 0
run_ba5 = 0
run_ba6 = 0
run_ba7 = 0
run_ba8 = 0
run_ba9 = 0
run_ba10 = 0
run_ba11 = 0


bowler_name = input("Enter bowler name > " )


while balls > i:



    input1 = input("What happened on this ball ")
    if input1 == 'wide':
        run = run + 1

        extra = int(input("Extras > "))
        run_over = run_over + 1

        if extra != 0:
            run = run + extra
            run_over = run_over + extra
            if extra == 1:
                striker_change.striker_change(strike,non_strike,extra)


        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        if i > 0 and i % 6 == 0:
            over_by_over_run.append(run_over)
            bowler_runs.bowler_runs(run_over, bowler_name, team_2_players)
            bowler_name = input("Enter bowler name > ")
            run_over = 0

        continue

    elif input1 == 'no ball':
        run = run + 1
        run_over = run_over + 1
        extra = int(input("Extras > "))
        if extra != 0:
            run = run + extra
            run_over = run_over + extra

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        if i > 0 and i % 6 == 0:

            over_by_over_run.append(run_over)
            bowler_runs.bowler_runs(run_over, bowler_name, team_2_players)
            bowler_name = input("Enter bowler name > ")
            run_over = 0

        continue

    elif input1 == '1':
        run = run + 1
        run_over = run_over + 1
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        if i >= 0 and i % 6 == 0:
            over_by_over_run.append(run_over)
            bowler_runs.bowler_runs(run_over,bowler_name,team_2_players)
            bowler_name = input("Enter bowler name > ")
            run_over = 0

        continue

    elif input1 == '2':
        run = run + 2
        run_over = run_over + 2
        i = i + 1


        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")


        if i >= 0 and i % 6 == 0:
            over_by_over_run.append(run_over)
            bowler_runs.bowler_runs(run_over,bowler_name,team_2_players)
            bowler_name = input("Enter bowler name > ")
            run_over = 0


        continue

    elif input1 == '3':
        run = run + 3
        run_over = run_over + 3
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        if i >= 0 and i % 6 == 0:
            over_by_over_run.append(run_over)
            bowler_runs.bowler_runs(run_over,bowler_name,team_2_players)
            bowler_name = input("Enter bowler name > ")
            run_over = 0

        continue

    elif input1 == '4':
        run = run + 4
        run_over = run_over + 4
        i = i + 1


        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        if i >= 0 and i % 6 == 0:
            over_by_over_run.append(run_over)
            bowler_runs.bowler_runs(run_over,bowler_name,team_2_players)
            bowler_name = input("Enter bowler name > ")
            run_over = 0

        continue

    elif input1 == '6':
        run = run + 6
        run_over = run_over + 6
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        if i >= 0 and i % 6 == 0:
            over_by_over_run.append(run_over)
            bowler_runs.bowler_runs(run_over,bowler_name,team_2_players)
            striker_change.striker_change_2(strike,non_strike)
            bowler_name = input("Enter bowler name > ")
            run_over = 0

        continue

    elif input1 == "Wicket" or "wicket" or "W" or "w":
        wickets = wickets+1
        batsman_change.batting_order(team_1_players)
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        if i >= 0 and i % 6 == 0:
            over_by_over_run.append(run_over)
            bowler_runs.bowler_runs(run_over,bowler_name,team_2_players)
            # striker_change.striker_change_2(strike,non_strike)
            bowler_name = input("Enter bowler name > ")
            run_over = 0

        continue


print(over_by_over_run)
# plt.bar(over,over_by_over_run)
# plt.show()

if toss_winner == team_1:
    if toss_decision == "bat":
        print(f"the {toss_winner} has posted a target of {run} at a loss of {wickets} wickets")
else:
    print(f"the {toss_winner} has stopped the {team_2} at a target of {run} runs for {wickets} wickets")

print(f"{run}/{wickets}")



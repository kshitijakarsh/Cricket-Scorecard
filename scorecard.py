import toss
import batsman
import batsman_change


location = input("Location : ")


team_1 = input("Enter Team 1 Name ")
team_1_players = []

for i in range(11):
    players_team_1 = input(f"Enter player names {i} > ")
    team_1_players.append(players_team_1)

batsman.batsman(team_1_players)


team_2 = input("Enter Team 2 Name ")
team_2_players = []
for j in range(11):
    players_team_2 = input(f"Enter player names {j} > ")
    team_2_players.append(players_team_2)

batsman.batsman(team_2_players)

toss_winner = toss.toss_winner(team_1, team_2)
toss_decision = toss.toss_decision()

toss_looser = ''''''
if toss_winner == team_1:
    toss_looser == team_2
else:
    toss_looser == team_1

wickets = 0
over = int(input("Enter number of overs "))  # to enter the number of overs the match is going to be off
balls = over * 6



run = 0
i = 0
over_by_over_run = []
while balls >= i:

    if i!=0 and i%6==0:
        over_by_over_run.append(run)


    input1 = input("What happened on this ball ")
    if input1 == 'wide':
        run = run + 1
        extra = int(input("Extras > "))

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        if extra != 0:
            run = run + extra
        continue

    elif input1 == 'no ball':
        run = run + 1
        extra = int(input("Extras > "))
        if extra != 0:
            run = run + extra

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        continue

    elif input1 == '1':
        run = run + 1
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        continue

    elif input1 == '2':
        run = run + 2
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        continue

    elif input1 == '3':
        run = run + 3
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        continue

    elif input1 == '4':
        run = run + 4
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        continue

    elif input1 == '6':
        run = run + 6
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")

        continue

    elif input1 == "Wicket" or "wicket" or "W" or "w":
        wickets = wickets+1
        wicket_style = input("How did he get out > ")
        batsman_change.batting_order(team_1)
        i = i + 1

        overs = int(i / 6)
        over_ball = i % 6
        print(f"{overs} . {over_ball}")


print(over_by_over_run)

print(f"{run}/{wickets}")
if toss_decision == "bat":
    print(f"the {toss_winner} has posted a target of {run} at loss of {wickets} wickets")
else:
    print(f"the {toss_winner} has stopped the {toss_looser} at a target of {run} runs for {wickets} wickets")
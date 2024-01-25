def bowler_runs(runs, bowler_name, team_2_players):
    team_2_players = team_2_players
    run_b1 = 0
    run_b2 = 0
    run_b3 = 0
    run_b4 = 0
    run_b5 = 0


    if bowler_name == team_2_players[6]:
        run_b1 = run_b1 + runs
    elif bowler_name == team_2_players[7]:
        run_b2 = run_b2 + runs
    elif bowler_name == team_2_players[8]:
        run_b3 = run_b3 + runs
    elif bowler_name == team_2_players[9]:
        run_b4 = run_b4 + runs
    elif bowler_name == team_2_players[10]:
        run_b5 = run_b5 + runs

    return run_b1,run_b2,run_b3,run_b4,run_b5
import batsman_change

def striker_change(strike, non_strike, run):
    c = ""
    if run == 1 or run == 3:
        c = strike
        striker = non_strike
        non_striker = c
    print(striker)
    print(non_striker)

def striker_change_2(strike, non_strike):
    d = strike
    strike = non_strike
    non_strike = d
    print(strike)
    print(non_strike)

def striker_change_3(batsman,batsman2):
    strike = batsman
    non_strike = batsman2
    print(strike)
    print(non_strike)
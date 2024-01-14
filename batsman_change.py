def batting_order(team_1):
    batsman = ""
    batsman2 = ""
    i = 0
    length = len(team_1)
    wicket = 0
    while i <= length:
        b = input("Wicket fall")
        if b == "yes":
            wicket == wicket + 1
            i = i + 1
            if wicket <= 10:
                batsman = team_1[i]
                batsman2 = team_1[i + 1]
                print(batsman)
                print(batsman2)
                break
        elif b == "no":
            break

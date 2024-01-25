import striker_change
def batting_order(team_1):

    i = 0
    length = len(team_1)
    wicket = 0
    while i <= length:
        b = input("Wicket fall")
        if b == "yes":
            wicket == wicket + 1
            i = i + 1
            out = input("Who got out? > ")
            if wicket <= 10:
                team_1.remove(out)
                batsman = team_1[0]
                batsman2 = team_1[1]
                striker_change.striker_change_3(batsman,batsman2)
                # print(batsman)
                # print(batsman2)
                break
        elif b == "no":
            break

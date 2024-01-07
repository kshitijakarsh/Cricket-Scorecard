import playsound
from gtts import gTTS
import random
import batsman

location = input("Location : ")

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


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


speak(f"""Ladies and gentlemen, welcome to the electrifying atmosphere of {location} as we bring you live coverage of this highly anticipated cricket match between {team_1} and {team_2}. The stage is set, the players are ready, and the excitement is palpable as these two formidable teams prepare to battle it out on the field.

{team_1}, known for their explosive batting lineup and formidable bowling attack, are hungry for victory today. They've had a stellar season so far, and the fans are expecting nothing less than a spectacular performance from their cricketing heroes.

On the other side, {team_2}, a force to be reckoned with, are no strangers to success. With a balanced squad and a history of turning the tide in their favor, they enter the field with confidence and determination. The crowd is buzzing with anticipation as they eagerly await the clash of these cricketing titans.""")

teams = [team_1,team_2]
toss_winner = random.choice(teams)

decisions = ["bat","bowl"]
toss_decision = random.choice(decisions)

speak(f"""The coin has been tossed, and {toss_winner} has won the toss and elected to {toss_decision} first. The strategy is set, the game plan is in motion, and we're moments away from witnessing the first ball of this thrilling encounter.

The weather is perfect, the pitch looks promising, and we're in for a treat as some of the finest cricketers showcase their skills today. As we delve into this match, keep your eyes peeled for breathtaking boundaries, wicket-taking deliveries, and strategic gameplay that will keep you on the edge of your seats.

So, fasten your seatbelts, cricket enthusiasts, as we embark on this journey together. It's {team_1} versus {team_2} in a battle of skill, strategy, and sheer determination. Stay tuned for an unforgettable cricketing spectacle!""")


speak(f"We have the {team_1} whose line up will have players like")
for k in range(11):
    speak(team_1_players[k])

speak(f"We have the {team_2} whose line up will have players like")
for l in range(11):
    speak(team_2_players[l])

# speak(f"the batsmen from {team_1} are ")
# batter_1_len = len(batsman_team_1)
# for a in batter_1_len:
#     speak(batsman_team_1(a))




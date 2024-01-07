import playsound
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

input1 = input("What happens on this ball > ")
if input1 == "wicket" or "W":
    wicket_style = input("Wicket Style > ")
    speak(f"{Bowler_name} has taken a wicket. He {wicket_style}")


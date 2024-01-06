
import team
import playsound
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)






over = int(input("Enter number of balls ")) # to enter the number of overs the match is going to be off
balls = over*6
run = 0
i = 0
while balls>i:
    input1 = input("What happened on this ball ") 
    

    if input1 == 'wide':
        speak(input1)
        speak("the bowler has bowled a wide and awarded extra runs to the opposition, the bowler needs to catch his rythm back")
        run = run + 1
        extra = int(input("Extras > "))
        if extra == 0:
            speak("however it's nice they didn't give away any extras")
        else:
            speak(f"oh no they're being miserable here giving up {extra} more")
        
        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")
        
        
        if extra != 0:
            run = run + extra
        continue

    elif input1 == 'no ball':
        speak(input1)
        speak("the bowler has bowled a no-ball and awarded extra runs to the opposition, the bowler needs to catch his rythm back")
        run = run + 1
        extra = int(input("Extras > "))
        if extra != 0:
            run = run + extra

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")    
        
        continue

    elif input1 == '1':
        speak(f"{input1}run")
        run = run + 1
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

    elif input1 == '2':
        speak(f"{input1}run")
        run = run + 2
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

    elif input1 == '3':
        speak(f"{input1}run")
        run = run + 3
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

    elif input1 == '4':
        speak(f"{input1}run")
        run = run + 4
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

    elif input1 == '6':
        speak(f"{input1}run")
        run = run + 6
        i = i + 1

        overs = int(i/6)
        overball = i%6
        print(f"{overs} . {overball}")

        continue

print(run)
speak(f"the target for opposition is {run} runs")
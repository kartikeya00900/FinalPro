import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pywhatkit
import webbrowser



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Ash' in command:
                command = command.replace('Ash', '')
                print(command)
    except:
        pass
    return command


def run_bruno():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'what is' in command:
        question=command.replace('what is','')
        information=webbrowser.open(question)
        print(information)
        talk(question+'is')

    elif 'how are you' in command:
        talk("Im good thanks For Asking")

    elif 'addition' in command:
        c=int(input("Enter Number: "))
        c2=int(input("Enter 2nd Number: "))
        result=(c+c2)
        print(result)

    elif 'subtraction' in command:
        c=int(input("Enter Number: "))
        c2=int(input("Enter 2nd Number: "))
        result=(c-c2)
        print(result)


    elif 'division' in command:
        c=int(input("Enter Number: "))
        c2=int(input("Enter 2nd Number: "))
        result=(c/c2)
        print(result)
    

    elif 'power' in command:
        c=int(input("Enter Number: "))
        result=(c**2)
        print(result)

    elif 'text' in command:    
        text=input("Enter Message")
        #number=input("enter phone number")
        hour=int(input("Enter Hours In 24 hours Format"))
        min=int(input("Enter Mins In 24 hours Format"))
        number=command.replace('text','+91')
        pywhatkit.sendwhatmsg(number,text,hour,min)


   ### elif 'group chat' in command:    
        #gc=input("Enter Message")
        #number=input("enter phone number")
       # hour=int(input("Enter Hours In 24 hours Format"))
      #  min=int(input("Enter Mins In 24 hours Format"))
     #   link=command.replace('gc','')
       ### pywhatkit.sendwhatmsg_to_group('https://chat.whatsapp.com/KqzCW3mMgDeANi5MHPlJmD',gc,hour,min)

    else:
        talk('Please say the command again.')


while True:
    run_bruno()

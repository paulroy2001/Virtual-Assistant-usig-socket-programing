import socket
import pyttsx3
import speech_recognition as sr

#creating speak function using imported pyttsx3 library
def speak(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

#creating function to take commands using speech recognition library
def takeCommand():
    r=sr.Recognizer()
    while(True):
        with sr.Microphone() as source:    
            #pause threshold created so that after how much time speech hear is valid   
            r.pause_threshold=0.7
            audio=r.listen(source)
            #exceptions created so that when the mic can get a clear command
            try:
                Query=r.recognize_google(audio,language='en-in')
                print(Query)
                return Query

            except Exception as e:
                speak("Could u please repeat again?")

#created so that mich will be actively listening but not respond even if the command is valid or not
def takeCommand1():
    r=sr.Recognizer()
    while(True):
        with sr.Microphone() as source:     
            #pause threshold created so that after how much time speech hear is valid  
            r.pause_threshold=0.7
            audio=r.listen(source)
            #exceptions created so that when the mic can get a clear command
            try:
                Query=r.recognize_google(audio,language='en-in')
                print(Query)
                return Query
            except Exception as e:
                continue
    
#the infinite loop is created so that the program will run forever helping the user
while(True):
    q=takeCommand1().lower()
    #takes command by using the defined function of take command
    if "hey" in q or "jarvis" in q:
        #the program start interacting only when the call command jarvis or hey is heard 
        speak("Hello")
        speak("Welcome to Paul's customized dedicated Employee System..")
        speak("Please Direct me as your wish")
        #speak functions defined are used to talkback to the user
        #net infinte loop is activated for the functions which will be used in the future
        while(True):
            #socket gets intialized for the communication with the server side
            c=socket.socket()
            #it connects to the local host defined at 9999 port of the socket
            c.connect(("LocalHost",9999))
            #it takes command by using user defined fuctions
            query=takeCommand().lower()
            #the command taken is sent to the server to process and give the appropirate command back
            c.send(bytes(query,'utf-8'))
            #the talkback response from the server is recieved by the client from the server side
            x=c.recv(1024).decode()
            
            #exits the second infinite loop if one is there in reciever command
            if "one" in x:
                speak("please Call me again if you have anyother work")
                speak("I will be here assisting with you if have any")
                break
            
            else:
                speak(x)
                print(x)
                #asking for new command so that the process will be continously running according to the user
                speak("Do you want anything else boss?")
        
            
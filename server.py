import socket
import webbrowser
import datetime
import pyautogui
import os
import psutil
import pyjokes

#socket created initialized in the ip
s=socket.socket()

#letting the user know about the course
print("Socket Created") 

#binding the socket to the local host where the connection is created at 9999
s.bind(("LocalHost",9999))

#creating nof connections the server can handle simultaneously through the socket
s.listen(3)
#creating three connection for safety purpose

print("Waiting For Connetions")

#fuction being created here to convet the time which can be understood better
def convertTime(seconds):
    #dividing seconds by 60 for minutes
    minutes,seconds=divmod(seconds, 60)

    #dividing minutes by 60 for hours
    hours,minutes=divmod(minutes, 60)

    #returning the values
    return "%d:%02d:%02d"%(hours, minutes, seconds)


#infinite lop created
while True:
    #f=0 initalized so that if all the commands doesn't match it can show sum results in the web
    f=0

    #c is initialized and address is created 
    c,addr=s.accept()
    print("Connected With",addr)

    #q recives the commnd from the client side
    q=c.recv(1024).decode()

    #prints the command for furthur assistance
    print(q)

    #if the user has no other commands the givig client side to go dormant
    if "no" in q:
        c.send(bytes(" one ",'utf-8'))

        #f value changed to stop it from web searching
        f=1

    elif "date" in q:
        from datetime import datetime
        data=datetime.now()
        d=data.strftime('%m/%d/%Y')
        c.send(bytes(d,'utf-8'))

        #f value changed to stop it from web searching
        f=1
    
    elif "open" in q:
        if "chrome" in q or "google" in q:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            c.send(bytes("Chrome being opened for you sir....",'utf-8'))

        elif "edge" in q or "microsoft" in q:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk")
            c.send(bytes("ms edge being opened for you sir....",'utf-8'))
        
        elif "brave" in q:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk")
            c.send(bytes("Brave being opened for you sir....",'utf-8'))

        #f value changed to stop it from web searching    
        f=1  

    #check whether there is a mention of time in the command
    elif "time" in q:
        #importing datetime from datetime library in python
        from datetime import datetime

        #time getting the curent time from the system
        time= datetime.now()

        #just getting the minute and hour from the system
        current=time.strftime("%H:%M")

        #time being sent to the client side
        c.send(bytes(current,'utf-8'))

        #f value changed to stop it from web searching
        f=1

    #check whether there is mention of youtube and check the search
    elif "search" in q and "youtube" in q:

        #finding the where in command search is located
        n1=q.find("serach")

        #since search word has a lenght of 6 
        n1=n1+6

        #finding the where in command in youtube is located
        n2=q.find("in youtube")

        #importing pywhatkit and initializing as pwt
        import pywhatkit as pwt

        #playing the youtube video from the internet
        pwt.playonyt(q[n1:n2])

        #sending the appropirate message
        c.send(bytes("this is the result we got...",'utf-8'))

        #f value changed to stop it from web searching
        f=1

    #checking whether volume or sound is there in the command
    elif "volume" in q or "sound" in q:

        #checking whether increase is there in the command
        if "increase" in q:

            #pyautogui class from python is used to increase the volume by 10%
            pyautogui.press("volumeup",10)

            #sending the appropirate command back to the client
            c.send(bytes("Audio Volume Increased Succesfully...",'utf-8'))
        
        #checking whether mute is there in the command
        elif "mute" in q:
            #pyautogui class from python is used to mute the volume
            pyautogui.press("volumemute")

        #decreasing the volume
        else:
            #pyautogui class from python is used to reduce the colume by 10%
            pyautogui.press("volumedown",10)

            #sending the appropirate command back to the client
            c.send(bytes("Audio Volume decreased Succesfully...",'utf-8'))

        #f value changed to stop it from web searching
        f=1

    #checking whether battery or left is there in the command
    elif "battery" in q and "left" in q:

        #using psutil class to get the battery status using sensors from the devices
        battery=psutil.sensors_battery()

        #using user defined functions to convert no of seconds left in battery drinage
        s=str(convertTime(battery.secsleft))

        #sending the appropirate command back to the client
        s="the time remaining for battery drinage is"+s
        c.send(bytes(s,'utf-8'))

        #f value changed to stop it from web searching
        f=1
    
    #checking whether battery or left is there in the command
    elif "percent" in q and "battery" in q:

        #using psutil class to get the battery percent using sensors from the devices
        battery = psutil.sensors_battery()

        #finding the battery percent
        p=str(battery.percent)

        #sending the appropirate command back to the client
        p="Battery percentage is ..."+p
        c.send(bytes(p,'utf-8'))

        #f value changed to stop it from web searching
        f=1

    #checking whether joke is there in the command
    elif "joke" in q:

        #getting the joke from the pyjoke class imported from python
        joke = pyjokes.get_joke(language="en", category="neutral")

        #sending the joke to the client side
        c.send(bytes(joke,'utf-8'))

        #f value changed to stop it from web searching
        f=1
    
    #if f==0 then all the functions are not meant by the user is not avialable 
    #giving a result from the webrowser
    elif f==0:

        #openning to the webrowser and inputing search term and giving the result
        webbrowser.open(q)

        #sending the appropirate command back to the client
        c.send(bytes("this is the result i got",'utf-8'))
    c.close()
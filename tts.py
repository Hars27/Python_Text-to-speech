import webbrowser
import os
import time
import sys
import getpass
from gtts import gTTS
from mutagen.mp3 import MP3

my_file = "C:/Users/%USERNAME%/Desktop/TTS/bob.mp3" 

username = getpass.getuser() 

def repeat():
    while True:
        if os.path.isfile(my_file): 
            os.remove(my_file)
        else:
            None

        tts = gTTS(text = input("Hello there " + username + """. This program is
used to output the user's input as speech.
Please input something for the program to say: """)) 
        tts.save('bob.mp3') 
        os.system("start bob.mp3") 

        audio = MP3(my_file)
        audio_length = audio.info.length 
        time.sleep((audio_length) + 0.25) 
        os.system('TASKKILL /F /IM wmplayer.exe') 
        time.sleep(0.5) 

        while True:
            answer = input("Do you want to repeat? (Y/N) ")
            if answer == "y" or answer == "Y":
                return repeat() 
            elif answer == "n" or answer == "N":
                if os.path.isfile(my_file): 
                    os.remove(my_file)
                else:
                    None
                sys.exit() 
            else:
                print("Sorry, I didn't understand that. Please try again with either Y or N.")
                continue 

repeat() #Calls the function.

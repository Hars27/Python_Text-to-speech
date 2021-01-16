import webbrowser
import os
import time
import sys
import getpass
from gtts import gTTS
from mutagen.mp3 import MP3

my_file = "C:/Users/%USERNAME%/Desktop/TTS/bob.mp3" #Sets a variable for the file path.

username = getpass.getuser() #Gets the username of the current user.

def repeat():
    while True:
        if os.path.isfile(my_file): #Checks to see whether there is a file present and, if so, removes it.
            os.remove(my_file)
        else:
            None

        tts = gTTS(text = input("Hello there " + username + """. This program is
used to output the user's input as speech.
Please input something for the program to say: """)) #Takes the user's input and uses it for the Text-To-Speech
        tts.save('bob.mp3') #Saves a .mp3 file of the user's input as speech.
        os.system("start bob.mp3") #Opens the .mp3 file

        audio = MP3(my_file) #Sets a variable so that the Mutagen module knows what file it's working with.
        audio_length = audio.info.length #Sets a variable of the length of the .mp3 file.
        time.sleep((audio_length) + 0.25) #Waits until the file has finished playing.
        os.system('TASKKILL /F /IM wmplayer.exe') #Closes Windows Media Player.
        time.sleep(0.5) #Waits until Windows Media Player has closed.

        while True:
            answer = input("Do you want to repeat? (Y/N) ")
            if answer == "y" or answer == "Y":
                return repeat() #Goes back to the beginning of the function if the user wants to try again.
            elif answer == "n" or answer == "N":
                if os.path.isfile(my_file): #Checks to see whether there is a file present and, if so, removes it.
                    os.remove(my_file)
                else:
                    None
                sys.exit() #Exits the program.
            else:
                print("Sorry, I didn't understand that. Please try again with either Y or N.")
                continue #Goes back to the beginning of the while loop.

repeat() #Calls the function.

#Downloads clips from twitch using youtube-dl 
from os.path import isdir
from streamers import streamer_list
import os
import pyautogui

#Create clips directory
def createDirectories():
    workingDirectory = os.getcwd()
    clipDirectory = workingDirectory+"\Clips"
    if (os.path.isdir(clipDirectory)): #If clip directory exists
        for streamer in streamer_list:
            if (os.path.isdir(clipDirectory+streamer)): #If streamers folder exists
                pass
            else:
                os.makedirs(streamer)
    else:
        os.makedirs("Clips")

#Get clips url
def createClipsUrls():
    url =""
    range = "7d"
    for streamer in streamer_list:
        url = "https://www.twitch.tv/"
        url += streamer
        url += "/videos?filter=clips&range="
        url += range
        print("Final url:", url)
        url = ""

#Download clip from twitch
def downloadClip():
    os.system("cd Clips & cd Channel & youtube-dl.exe -f best https://www.twitch.tv/flashgamesnemesis/clip/RespectfulEsteemedMetalNotATK")

def main():
    createDirectories()
    #createClipsUrls()

if __name__ == "__main__":
    main()
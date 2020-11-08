#Downloads clips from twitch using youtube-dl 
from os.path import isdir

from pyautogui import sleep
from streamers import streamer_list
import os
import time
from selenium import webdriver

driver = webdriver.Chrome("D:\Varios\Python 3\Scripts\chromedriver.exe")

#Create clips directory
def createDirectories():
    workingDirectory = os.getcwd()
    clipDirectory = workingDirectory+"\Clips"
    if (os.path.isdir(clipDirectory)): #If clip directory exists
        for streamer in streamer_list:
            if (os.path.isdir(clipDirectory+"\\"+streamer)): #If streamers folder exists
                pass
            else:
                os.makedirs(clipDirectory+"\\"+streamer)
    else:
        os.makedirs("Clips")
        createDirectories()

#Get clips url
def createClipsUrls():
    url = ""
    urlList = []
    range = "7d"
    for streamer in streamer_list:
        url = "https://www.twitch.tv/"
        url += streamer
        url += "/videos?filter=clips&range="
        url += range
        urlList.append(url)
        url = ""
    return urlList

def getClipToDownload():
    urlList = createClipsUrls()
    driver.maximize_window()
    for url in urlList:
        #Go to the url, get the urls for the first 5 clips.
        #Here selenium starts
        driver.get(url)
        sleep(5)
        pass

#Download clip from twitch
def downloadClip(streamer, clipUrl):
    downloadCommand = "cd Clips & cd "+streamer+" & youtube-dl.exe -f best "+clipUrl
    os.system(downloadCommand)

def main():
    getClipToDownload()

if __name__ == "__main__":
    main()
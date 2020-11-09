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
    clipList=[]
    driver.get("https://www.twitch.tv/")
    driver.maximize_window()
    sleep(8)
    for url in urlList:
        #Go to the url, get the urls for the first 5 clips.
        driver.get(url)
        driver.maximize_window()
        sleep(4)
        xPathTemp = "//*[@id=\"root\"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div["
        for i in range(1,6):
            clipSite = driver.find_element_by_xpath(xPathTemp + str(i) +"]")
            clipSite.click()
            sleep(1)
            clipList.append(driver.current_url)
            sleep(0.2)
            driver.back()
    driver.quit()
    return clipList

#Download clip from twitch
def downloadClip():
    clipList = getClipToDownload()
    for streamer in streamer_list:
        for clipUrl in clipList:
            downloadCommand = "cd Clips & cd "+streamer+" & youtube-dl.exe -f best "+clipUrl
            os.system(downloadCommand)

def main():
    createDirectories()
    downloadClip()

if __name__ == "__main__":
    main()
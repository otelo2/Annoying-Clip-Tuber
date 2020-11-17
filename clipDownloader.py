#Downloads clips from twitch using youtube-dl 
from os.path import isdir
import selenium
from streamers import streamerList
from clips import clipList
import os
from time import sleep
from selenium import webdriver
from multiprocessing.dummy import Pool as ThreadPool

#Create clips directory
def createDirectories():
    workingDirectory = os.getcwd()
    clipDirectory = workingDirectory+"\Clips"
    if (os.path.isdir(clipDirectory)): #If clip directory exists
        for streamer in streamerList:
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
    for streamer in streamerList:
        url = "https://www.twitch.tv/"
        url += streamer
        url += "/videos?filter=clips&range="
        url += range
        urlList.append(url)
        url = ""
    return urlList

def getClipToDownload(numClips):
    driver = webdriver.Chrome("D:\Varios\Python 3\Scripts\chromedriver.exe")
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
        for i in range(1,numClips+1):
            clipSite = driver.find_element_by_xpath(xPathTemp + str(i) +"]")
            clipSite.click()
            sleep(1)
            clipList.append(driver.current_url)
            sleep(0.2)
            driver.back()
    driver.quit()
    clipFile = open("ClipsUrls.txt","w")
    for c in clipList:
        clipFile.write(c+"\n")
    clipFile.close()

#Download clip from twitch
def downloadClip(clipsToDownload):
    count=0
    streamer = 0
    for clipUrl in clipList:
        try:
            downloadCommand = "cd Clips & cd "+streamerList[streamer]+" & youtube-dl.exe -f best "+clipUrl
            os.system(downloadCommand)
            print("\n")
            count +=1
            if ((count) % clipsToDownload == 0):
                streamer += 1
                print("\n")
        except IndexError as e:
            print("Finished downloading every clip.")
            break


def main():
    createDirectories()
    selection = int(input(" 1. Add clips to list \n 2. Download clips \n 3. Add and download clips\n"))
    if selection == 1:
        clipsToDownload = int(input("How many clips do you want to download?\n"))
        getClipToDownload(clipsToDownload)
    elif selection == 2:
        #This shouldn't work like this, fix later
        clipsToDownload = int(input("How many clips do you want to download?\n"))
        #pool = ThreadPool(clipsToDownload)
        #results = pool.map(downloadClip, )
        downloadClip(clipsToDownload)
    elif selection == 3:
        clipsToDownload = int(input("How many clips do you want to download?\n"))
        getClipToDownload(clipsToDownload)
        downloadClip(clipsToDownload)
    else:
        print("ok bye lmao")


if __name__ == "__main__":
    main()
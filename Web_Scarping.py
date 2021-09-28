
#import modeul and package

import csv
from pickletools import optimize
from matplotlib.pyplot import xlabel
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest

titleData = []
companyData = []
locationData = []
type_jobData = []

def setLinkForWebPage(link="Unknown"):
    sendRequest = requests.get(link) 
    contentWebPage = sendRequest.content
    return contentWebPage

def optimizeDataFromWebPage(setLinkForWebPage ="Unknown"):
    optimizeData = BeautifulSoup(setLinkForWebPage,"lxml")
    
    title = optimizeData.find_all("h2",{"class":"css-m604qf"})
    company = optimizeData.find_all("a",{"class":"css-17s97q8"})
    location = optimizeData.find_all("span",{"class":"css-5wys0k"})
    type_job = optimizeData.find_all("div",{"class":"css-1lh32fc"})
    
    for collectionData in range(len(title)):
        titleData.append(title[collectionData].text)
        companyData.append(company[collectionData].text)
        locationData.append(location[collectionData].text)
        type_jobData.append(type_job[collectionData].text)
        
def createFileCsv ():
    # list_File = [titleData , companyData , locationData , type_jobData]
    # unpuckingData = zip_longest(*list_File)
    with open("E:/Scarping Data/dataWuzzuf.csv", "w") as DataFile:
         collectionDataFile = csv.writer(DataFile)
         collectionDataFile.writerow(["TITLE" , "COMPANY" , "LOCATION" , "TYPE_JOb"])
         collectionDataFile.writerows([titleData , companyData , locationData , type_jobData])
        #  collectionDataFile.writerows(unpuckingData)
         
optimizeDataFromWebPage(setLinkForWebPage("https://wuzzuf.net/search/jobs/?q=data+analysit&a=hpb"))
createFileCsv()


import requests
from bs4 import BeautifulSoup
import json
import re


def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

class Crawler():
    def __init__(self,url):
        self.url=url
        self.soup=None

    def request(self):
        r=requests.get(self.url)
        self.soup=BeautifulSoup(r.text,'lxml')

    def getPrice(self):
        for i in self.soup.findAll(class_='hardfacts clear'):
            for k in i.findAll(class_='ng-star-inserted'):
                print(k.text)



    def getPhoneNumber(self):
        xd=""
        for x in self.soup.findAll('script')[-1]:
            xd=str(x)
            break
        x=xd.split(';')
        for i in x:
            if sum(k.isdigit() for k in i)>=9 and sum(k.isdigit() for k in i)<=12:
                print(i)
                break

    def getBrokerName(self):
        for i in self.soup.findAll(class_="iw_left"):
            x=i.find('p')
            if x is not None:
                if x.find('strong') is not None:
                    print(x.find('strong').text)

obj=Crawler(url='https://www.immowelt.de/expose/22rm95d')
obj.request()
obj.getBrokerName()
#hello
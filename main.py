import requests
from bs4 import BeautifulSoup
import json


class Crawler():
    def __init__(self,url):
        self.url=url
        self.soup=None

    def request(self):
        r=requests.get(self.url)
        self.soup=BeautifulSoup(r.text,'lxml')

    def getPrice(self):
        # for i in self.soup.findAll(class_='hardfacts clear'):
        #     for k in i.findAll(class_='ng-star-inserted'):
        #         print(k.text)
        x=self.soup.findAll('script')[-1].text
        print([int(s) for s in x.split() if s.isdigit()])

obj=Crawler(url='https://www.immowelt.de/expose/2228f53')
obj.request()
obj.getPrice()
import requests
import re
 
from bs4 import BeautifulSoup

url = "https://www.udemy.com/course/curso-online-certificacao-linux-lpic1-comptia/"

r = requests.get(url)

soup = BeautifulSoup(r.content,features='lxml')


tabelaDevalores = soup.find('div', class_=re.compile('curriculum--content--*'))

for valores in tabelaDevalores:

    sectionName = valores.find('div', class_=re.compile('section--section-title--*'))
    sectionPreviwedList = valores.findAll('div', class_=re.compile('section--lecture-title-and-description--*'))
    print(sectionName.next)
    print(" ")
    for sectionPreviwedItem in sectionPreviwedList:
        print(sectionPreviwedItem.text)
    print(" ")




 
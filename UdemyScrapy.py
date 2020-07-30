import requests
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
option = Options()
driver = webdriver.Firefox(options=option)
driver.get("https://www.udemy.com/course/curso-python-3-completo/")
time.sleep(20)
driver.find_element_by_xpath("//*[@id='br']//div[2]//div[3]//div[1]//div[4]//div[3]//div//div//div//div//button").click()
element = driver.find_element_by_xpath("//*[@id='br']//div[2]//div[3]//div[1]//div[4]//div[3]//div//div//div//div//div[3]")
html_content = element.get_attribute('outerHTML')
#variables
curso = []
item = {}
#BeautifulSoup magic to get content of list in udemy
soup = BeautifulSoup(html_content,features='lxml')
tableOfValues = soup.find('div', class_=re.compile('curriculum--content--*'))
#iterate in each atribute to get the property values
for values in tableOfValues:
    #Get the title of the section
    sectionName = values.find('div', class_=re.compile('section--section-title--*'))
    #Get all items of the section
    sectionPreviwedList = values.findAll('div', class_=re.compile('section--lecture-title-and-description--*'))
    #start to create a list with all values
    item['Type'] = "Section Header"
    item['Value'] = sectionName.next
    #adding header of an section
    curso.append(item.copy())
    for sectionPreviwedItem in sectionPreviwedList:
        item['Type'] = "Section List"
        item['Value'] = sectionPreviwedItem.text
        #adding items of an section
        curso.append(item.copy())
for item in curso:
    if item['Type'] == 'Section Header':
        if curso.index(item) == 0:
            print(item['Value'])
            print(" ")
        else:
            print(" ")    
            print(item['Value'])
            print(" ")

    else:
        print(item['Value'])

driver.quit()


 
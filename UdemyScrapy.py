import requests
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import os 

class Trello:
    def __init__(self):
        self.key = os.environ['key']
        self.token = os.environ['token']
class Course:
    def __init__(self,url):
        self.url = url
        self.name = self.getName(url)
        self.buttonXPath = "//button[@data-purpose='show-more']"
        self.contentXPath = "curriculum--content--PkBXH"   
        self.sections = []

    def getCourse(self, tableOfValues):
        for value in tableOfValues:
            sectionName = value.find('div', class_=re.compile('section--section-title--*'))
            sectionPreviwedList = value.findAll('div', class_=re.compile('section--lecture-title-and-description--*'))
            section = Section(sectionName.next)
            for sectionPreviwedItem in sectionPreviwedList:
                item = Item(sectionPreviwedItem.text)
                section.addSectionItem(item)
            self.addSection(section)
        return self

    def soupUdemy(self):
        option = Options()
        driver = webdriver.Firefox(options=option)
        driver.get(self.url)
        time.sleep(10)
        self.verifyIfButtonExists(driver)
        element = driver.find_element_by_class_name(self.contentXPath)
        html_content = element.get_attribute('outerHTML')
        soup = BeautifulSoup(html_content,features='lxml')
        tableOfValues = soup.find('div', class_=re.compile('curriculum--content--*'))
        curso = self.getCourse(tableOfValues)
        return curso
        
    def getName(self, url):
        nomeCurso = str(url)
        nomeCurso = self.retirarPrimeiroBarra(url)
        nomeCurso = nomeCurso.split('/')[4]
        nomeCurso = nomeCurso.replace('-',' ')
        return nomeCurso

    def retirarPrimeiroBarra(self, url):
        nomesembarra = str(url)
        if nomesembarra.endswith("/"):
            nomesembarra = nomesembarra[:-1]
            return nomesembarra
        else:
            return str(url)

    def verifyIfButtonExists(self,driver):
        try:
            driver.find_element_by_xpath(self.buttonXPath).click()            
        except:
            print("Não possui classe button")

    def addSection(self, section ):
        self.sections.append(section)
        
class Section():
    items = []
    def __init__(self,name):
        self.name = name

    def addSectionItem(self, name):
        item = Item(name)
        self.items.append(item)

class Item():
    def __init__(self,name):
        self.name = name      

url = "https://www.udemy.com/course/gestao-financeira/"
curso = Course(url)
valores = curso.soupUdemy()
print(curso.name)

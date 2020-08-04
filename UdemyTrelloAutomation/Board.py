import requests
import json
import os 
import Lista

class Board():

    def __init__(self,trelloBoardLink):
        self.key = os.environ['key']
        self.token = os.environ['token']
        self.boardID = self.getBoadId(trelloBoardLink)
        self.lists = []
        self.lists = self.getListBoard()
    
    
    def getBoadId(self,trelloBoardLink):
        trelloboardid = str(trelloBoardLink)
        trelloboardid = trelloboardid.split('/b/')[1].split('/')[0]
        return trelloboardid
    
    
    def getListBoard(self):
        url = "https://api.trello.com/1/boards/"+self.boardID+"/lists"
        query = {'key': self.key,'token': self.token}
        response = requests.request("GET",url,params=query)
        response = json.loads(response.text)
        for lista in response:
            listasTrello = Lista.Lista(lista['id'],lista['name'])
            self.addList(listasTrello)          
        return response
    
    def addList(self, lista):
        self.lists.append(lista)

    def getListIdByName(self,nameLista): 
        for lista in self.lists:
            if lista['name'] == nameLista:
                return lista['id']

    def createCard(self,name,nameLista):
        url = "https://api.trello.com/1/cards"
        query = {'key': self.key,'token': self.token,'idList': self.getListIdByName(nameLista),'name': str(name).upper()}
        response = requests.request("POST",url,params=query)
    
    def getCardIdByName(self,nameLista,cardName):
        url = "https://api.trello.com/1/lists/" + self.getListIdByName(nameLista) + "/cards"
        query = {'key': self.key,'token': self.token}
        response = requests.request("GET",url,params=query)
        response = json.loads(response.text)
        for card in response:
            if card['name'] == cardName:
                return card['id']
    
    def createCkeckList(self,nameCard,nameCheckList,listName):
        url = "https://api.trello.com/1/cards/"+ self.getCardIdByName(listName,nameCard) +"/checklists"
        query = {'key': self.key,'token': self.token,'name':nameCheckList}
        response = requests.request("POST",url,params=query)
   
    def createCheckItem(self,cardName,checkListName,nameLista,nameCheckItem):
        url = "https://api.trello.com/1/checklists/"+ self.getCheckListIdbyname(cardName,checkListName,nameLista) +"/checkItems"
        query = {'key': self.key,'token': self.token,'name': nameCheckItem}
        response = requests.request("POST",url,params=query)

    def getCheckListIdbyname(self,cardName,checkListName,nameLista):
        url = "https://api.trello.com/1/cards/" + self.getCardIdByName(nameLista,cardName) + "/checklists"
        query = {'key': self.key,'token': self.token}
        response = requests.request("GET",url,params=query)
        response = json.loads(response.text)
        for checklistitems in response:
            if checklistitems['name'] == checkListName:
                valor = checklistitems['id']
                return valor
       


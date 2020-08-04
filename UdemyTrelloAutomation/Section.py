import Item

class Section(object):
    
    def __init__(self,name):
        self.name = name
        self.items = []

    def addSectionItem(self, item):
        self.items.append(item)
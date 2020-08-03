import Item

class Section():
    items = []
    def __init__(self,name):
        self.name = name

    def addSectionItem(self, name):
        item = Item.Item(name)
        self.items.append(item)
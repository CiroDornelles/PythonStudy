from threading import Thread
import Board

class threadChecklist(Thread):
    def __init__(self,section,curso,lista,board):
        Thread.__init__(self)
        self.section = section
        self.curso = curso
        self.lista = lista
        self.board = board
     
    def run(self):
        for checkitem in self.section.items:
            self.board.createCheckItem(self.curso.name.upper(),self.section.name,self.lista,checkitem.name)
 
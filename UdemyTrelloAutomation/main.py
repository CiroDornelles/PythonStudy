import Course
import Board
import trellothread

listOfthreads = []
lista = "Programação Ciro"
url = "https://www.udemy.com/course/curso-python-3-completo/"
curso = Course.Course(url).soupUdemy()
board = Board.Board("https://trello.com/b/8JMJ83ie/estudos")
board.createCard(curso.name,lista)
for checklist in curso.sections:
    board.createCkeckList(curso.name.upper(),checklist.name,lista)
    
for section in curso.sections:   
    sectionThread = trellothread.threadChecklist(section,curso,lista,board)
    listOfthreads.append(sectionThread)

for thread in listOfthreads:
    thread.start()
for thread in listOfthreads:
    thread.join()


print("curso adicionado ao trello")

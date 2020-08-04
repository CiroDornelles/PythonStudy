import Course
import Board
lista = "Programação Ciro"
url = "https://www.udemy.com/course/curso-python-3-completo/"
curso = Course.Course(url).soupUdemy()
board = Board.Board("https://trello.com/b/8JMJ83ie/estudos")
board.createCard(curso.name,lista)
for checklist in curso.sections:
    board.createCkeckList(curso.name.upper(),checklist.name,lista)
    for checkitem in checklist.items:   
        board.createCheckItem(curso.name.upper(),checklist.name,lista,checkitem.name)



print("curso adicionado ao trello")

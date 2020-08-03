
import Course
import Trello
 
url = "https://www.udemy.com/course/gestao-financeira/"
curso = Course.Course(url)
valores = curso.soupUdemy()
print(curso.name)

from abc import ABC
class Animal(ABC):
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("I can walk and run")
class snake(Animal):
    def move(self):
        print("I can crawl")
class dog(Animal):
    def move(self):
        print("I can bark and run")
class lion(Animal):
    def move(self):
        print("I can roar and run") 
R=human()
R.move()
S=snake()   
S.move()
D=dog()
D.move()
L=lion()
L.move()    

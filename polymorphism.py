class cat:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def info(self):
      print(f"My name is {self.name }i am {self.age}years old")
    def makesound(self):
       print("meow")

class dog:
   def __init__(self,name,age):
        self.name= name
        self.age= age
   def info(self):
      print(f"My name is {self.name }i am {self.age}years old")
   def makesound(self):
       print("bark")
obj1= cat("bluey",5)
obj2= dog("Bingo",10)

for animal in(obj1,obj2):
    animal.info()
    animal.makesound()





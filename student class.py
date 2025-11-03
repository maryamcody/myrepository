class Person:
    def __init__ (self,firstname,lastname ):
        self.fname =firstname
        self.lname =lastname
    def display(self):
     print(self.fname,self.lname)
class Student(Person):
   def __init__(self, fname ,lname, year):
    self.year =year
    super().__init__(fname,lname)
obj=Student("Maryam","Abdulhakim",2026)
obj.display()
      
    
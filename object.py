class student:
   grade= 10
   name="Mary"
   
   def introduce(self):
    print("Hi i am a student")
   def details(self):
    print("My name is", self.name)
    print("I am in grade", self.grade)  

ob=student()
ob.introduce()
ob.details()
        
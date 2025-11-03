class dad:
    def __init__(self,eye,hair):
        self.eye=eye
        self.hair=hair
    def display_dad(self):
        print("Dad's eye color" ,self.eye)
        print("Dad's hair " ,self.hair)
class son(dad):
    def __init__(self, name ,age,hair,eye):
        self.name=name
        self.age=age
        dad.__init__(self,eye,hair)

obj =son("John",18,"black","brown")
obj.display_dad()

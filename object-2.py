class parrot:
  species ="birds"

  def __init__(self,name,age):
    self.name=name
    self.age=age
blue=parrot("Bluie",10)
Woo=parrot("Woo",15)
print("{} is a {} and is {} years".format(blue.name,blue.species,blue.age))
print("{} is a {} and is {} years".format(Woo.name,Woo.species,Woo.age))

 

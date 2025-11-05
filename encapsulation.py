class computer :
   def __init__(self):
      self.__maxprice=800
   def display(self):
    print("selling price ",self.__maxprice)
   def newmaxprice(self,price):
     self.__maxprice =price
c=computer()
c.display()
c.__maxprice =1000
c.display()
c.newmaxprice(1000)
c.display()





def fun1(n):
  return n*(n+1)/2
a = int(input("Enter a number: "))
print(fun1(a))

def fun2(n):
  sum = 0
  for i in range(1,n+1):
    sum += i
  return sum
a = int(input("Enter a number: "))
print(fun2(a))

def fun3(n):
  sum=0
  c=0
  for i in range(1,n+1):
     for j in range(1,i+1):
       sum+=1
       c+=1
  print("Count of operations:",c)
  return sum
a = int(input("Enter a number: "))
print(fun3(a))

    



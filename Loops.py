n= int(input("Enter a number:"))

for i in range(1,11):
    print (f"{n}x{i}={n*i}")

n=int(input('Enter number of rows:'))
for j in range(1,n+1):
    for k in range(j):
        print('*' ,end=' ')
    print()

n=int(input("Enter a number:"))
for i in range(2,n-1):
    if n%i==0:
        print(f"{n} is not a prime number")
        break
else:
        print(f"{n} is a prime number") 
     

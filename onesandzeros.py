def onesandzeros(n):
    ones=0
    zero=0
    while(n):
     if (n&1==1):
      ones+=1
     else:
       zero+=1
     n>>=1
    print("\n\nOnes=", ones,"\n\nZeros=",zero)
number=int(input("Enter a number "))
onesandzeros(number)

print

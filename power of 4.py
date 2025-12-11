def power4(num):
    count=0
    if (num &(~(num& (num-1)))==num):
        while num>1:
            num>>=1
            count+=1
        if (count %2==0):
            return True
        else:
            return False
num=int(input("Enter a number "))
if power4(num):
    print("The number is power of 4")
else:
    print("The number is not power of 4")
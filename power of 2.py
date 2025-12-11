def power2(num):
    if num==0:
        return 0
    if (num & (~(num -1))==num):
        return 1
num=int(input("Enter a number "))
if power2(num):
    print("The number is power of 2 ")
else:
    print("the number is not power of 2")
    
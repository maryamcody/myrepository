def setornotset(number,n):
    if number &(1<<(n-1)):
        print("\nSet")
    else:
        print("\nNotset")
number=int(input("Enter a number "))
n=int(input("Enter bit number "))
setornotset(number,n)
    
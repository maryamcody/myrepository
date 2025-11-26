def prints(n):
    if(n<=0):
        return
    print("codingal")
    prints(n/2)
    prints(n/2)
n=int(input("Enter a number: "))
prints(n)


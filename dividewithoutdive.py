def divide(ourdividend,ourdivisior):
    sign=(-1 if((ourdividend <0 )^(ourdivisior<0))else 1)
    ourdivisior=abs(ourdivisior)
    ourdividend=abs(ourdividend)
    quotientNumber=0
    tempNumber=0
    for i in range(31,-1,-1):
        if (tempNumber + (ourdivisior<<i) <=ourdividend):
            tempNumber += ourdivisior<< i
            quotientNumber|=1<< i
    if sign == -1:
        quotientNumber =- quotientNumber
    return quotientNumber
a =int(input("Enter a number"))
b=int(input("Enter the second number "))
print("Result =",divide(a,b))
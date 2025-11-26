def sum(n):
    return n*(n+1)/2
#space complexity is 0(1), aulixiliary space is 0(1)

def arraysum(a):
    sum=0
    for i in a:
        sum=sum+1
    return (sum)
a=[12,3,4,5,6]
arraysum(a)
 
 #space complexity is 0(n), aulixiliary space is 0(1)

def summ(n):
    if(n<=0):
        return 
    return n+ summ(n-1)

def onsquaretime(n):
    iteration = 0
    print("Number entered by user is:", n)
    for i in range(0, n):
        for j in range(0,n):
            iteration+=1
            
            print("*", end=" ")
        print()
    print("Total number of iterations is:", iteration)
onsquaretime(10)
onsquaretime(5)
print("\n with any 'n' the time will change significantly")
print("0(n^2)")

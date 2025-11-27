def factor(n):
    for i in range(1, n + 1):
        if n % i == 0:
          print(i)
input_num = int(input("Enter a number to find its factors: "))
print(factor(input_num))



            


            
    
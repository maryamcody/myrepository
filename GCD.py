biggest_number=int(input("Enter first number: "))
smallest_number=int(input("Enter second number: "))

while(smallest_number):
    temp=smallest_number 
    smallest_number=biggest_number%smallest_number
    biggest_number=temp

print("The GCD is ",temp)


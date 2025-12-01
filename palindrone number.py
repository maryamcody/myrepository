number=int(input("Enter a number: "))
digit_number=number
reverse_number=0

while number>0:
    digit=number%10
    reverse_number=reverse_number*10+digit
    # to collect a quotient
    number//=10
if digit_number==reverse_number:
    print(f"{digit_number} is a palindrome number")
else:
    print(f"{digit_number} is not a palindrome number")
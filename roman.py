def romantoint(n):
    roman={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultiteration=0
    for i in range(0, len(n)-1):
        if roman[n[i]]<roman[n[i+1]]:
            resultiteration -= roman[n[i]]
        else:
            resultiteration += roman[n[i]]
    return resultiteration + roman[n[-1]]
input_roman = input("Enter a Roman numeral: ")
print(romantoint(input_roman))


        
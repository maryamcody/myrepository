input =open("updated.txt","w")
output=open("repeated.txt","r")

temp= set()
print("Elimate duplicate lines ")
for line in output:
    if line not in temp :
       input.write(line)
       temp.add(line)
input.close()
output.close()
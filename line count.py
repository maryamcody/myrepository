content = open("codingal.txt","r")
counter= 0
mycontent= content.read()
colist =mycontent.split("\n")
#\n is  new line charcter
for i in colist:
    if i:
        counter += 1
print("number of lines",counter)

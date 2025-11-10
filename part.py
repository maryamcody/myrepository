f1=open("firstfile.txt","r")
f2=open("secondfile.txt","w")
cont =f1.readlines()
for i in range(1,len(cont)+1):
    if i % 2 ==0:
      f2.write(cont[i-1])

    else :
       pass
f1.close()
f2.close()




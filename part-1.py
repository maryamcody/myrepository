f1 =open ("firstfile.txt","r")
f2 =open ("secondfile.txt","a")

for line in f1.readlines():
    print(line)
    if (line.startswith("Coding")):
        print(line)
        f2.write(line)

f1.close()
f2.close()
file_read=open("codingal.txt","r")
print(file_read.read())
file_read.close()
print("add new content inside the file")


file_write= open("codingal.txt","w")
file_write.write("file in write mode ...")
file_write.write(" Hi i am Maryam .I am 2 years old")
file_write.close()

file_write= open("codingal.txt","a")
file_write.write("file in append mode ...")
file_write.write(" Hi i am Mary .I am 10 years old")
file_write.close()

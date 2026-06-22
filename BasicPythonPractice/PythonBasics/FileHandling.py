#FileHandling.
#reading or saving data from files.

file = open("../OtherFiles/Data01.txt","r")
content = file.read()
print(content)
file.close()

#to automatically close the file.
with open("../OtherFiles/Data01.txt","r") as file2:
    content2 = file2.read()
    
print(content2)

#to write in a file.
with open("../OtherFiles/Data01.txt","w") as file3:
    content3 = file3.write("This is just me appending some random stuff into it.")

#to append data.
with open("../OtherFiles/Data01.txt","a") as file3:
    content3 = file3.write("\nAppending some other stuff")

print(content)
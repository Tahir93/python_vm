#reading from a text file
with open("test.txt","r") as file:
    content = file.read()
#print(content)

#writing to a file
with open("test.txt","w+") as file:
    file.write("This is new text written in append mode")
    file.seek(0)        #moves the pointer to 0 index
    content = file.read()
print(content)
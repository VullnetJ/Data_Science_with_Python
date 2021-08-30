#file = open("fruit.txt")

# content = file.read()
# file.close() // if you close 
# second = file.read() // cant call again because it will produce an error
# print(content)
# print(second)

# with open("fruit.txt", "r") as Fruits: # it closes itself once it is executed
#     content = Fruits.read() # if not stated it is automatically "r" read.  "r" for reading, "w" for writing
# print(content)

with open("written.txt", "a+") as cont:
    cont.write("\nBlueBerry\nStrawberry")
    cont.seek(1) # to position the coursor at the beggining
    read_it = cont.read()
print(read_it)

file = open("test.txt")

# this will help you to read contents of text file
#print(file.read())
# if you want specific characters of the text file
#print(file.read(7))
# read line method to read single line at a time
#print(file.readline())
#print(file.readline())
#print(file.readline())

# print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# reading a file using readlines method

values = file.readlines()
for i in values:
    print(i)
file.close()
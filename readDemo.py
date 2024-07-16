file = open('test.txt')
#print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

line = file.readlines()
for i in line:
    print(i)


file.close()


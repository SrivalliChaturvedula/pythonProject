# opening and closing a file in python
# read the file and store all lines in list
# reverse the list
with open("test.txt", 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open("test.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)








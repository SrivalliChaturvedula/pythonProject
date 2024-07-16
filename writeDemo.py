# read the lines and store in list
# reverse the list
# write reversed list back to  file

with open("test.txt", 'r') as reader:
    values = reader.readlines()
    reversed(values)
    with open('test.txt', 'w') as writer:
        for line in reversed(values):
            writer.write(line)

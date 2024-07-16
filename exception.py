

itemsinCart = 0

if itemsinCart != 2:
    # raise Exception("Products count did not match as expected")
    pass

#assert (itemsinCart == 2)
# try, except block

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except:
    print('text file could not be found')

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("cleaning up resources")



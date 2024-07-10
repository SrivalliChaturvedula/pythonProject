# Declaring int value
a = 10
print(a)
# To get the data type of a variable
print(type(a))
# float value
b = 0.98
print(b)
print(type(b))
print(a+b)
c = 10+2j
print(c)
print(type(c))
d = 5
#Declaring string value
name = "Shanvitha"
name2 = "Jyotsna"
print(name, name2)
print("Name of elder kid is " + name2 + " and the name of second kid is " + name)
# Concatinating two data types
print("{} {}".format("Name is " + name2 + " Age is ", a))
print("{} {}".format("Name is " + name + " Age is", d))

# List is a datatype that allows multiple values with different data types. Index of list starts with 0.
values = [1, 2, "rahul", 4, 5]
print(values)
# Printing value of list in the particular index
print(values[0]) #1
print(values[-1]) #5
print(values[1:3]) #2, 'rahul'
values.insert(3,"Shetty") # Adding
print(values)
values.append(6)
print(values)
values[2] = "RAHUL"
print(values) # updating
del values[0] # deleting
print(values)

# Tuple declaration
tup = (1, 2, "Sri", 4, 5)
print(tup)
# tup[2] = "valli" value changing is not accepted in tuples, it is immutable

# Dictionary declaration
dic = {"a": 2, 4: "bcd", "c": "Hello world"}
print(dic)
print(dic[4]) # values are accessed with key of the dictionary
print(dic["a"])

# Creating dictionary at runtime
dict = {}
print(dict)

dict["first name"] = "Sri"
dict["last name"] = "Valli"
dict["age"] = 32
dict[123] = 456
print(dict)

print(dict['first name'])
print(dict[123])



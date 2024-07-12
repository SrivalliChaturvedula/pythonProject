str1 = "RahulShettyAcademy.com"
str2 = " Testing platform "
str3 = "Shetty"
print(str1[1])  # printing single character of string using index
print(str1[5:11])  # printing number of characters of string using index
print(str1 + str2)  # concatenating two strings
print(str3 in str1)  # comparing string/ substring check

var = str1.split(".")
print(var)
print(var[0])

str4 = "   great  "
print(str4)
var2 = str4.strip() # removes spacing
print(var2)
print(str4.lstrip()) # removes left spacing
print(str4.rstrip())  # removes right spacing


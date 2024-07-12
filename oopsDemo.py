class Calculator():
    num = 100  # class variable

    # default constructor
    def __init__(self, a, b):
        print("Im called automatically when an object is created")
        self.firstNumber = a
        self.secondNumber = b

    def getdata(self):
        print("Im executing a method in a class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)
print(obj.getdata())
print(obj.summation())

obj1 = Calculator(4, 5)
print(obj1.summation())

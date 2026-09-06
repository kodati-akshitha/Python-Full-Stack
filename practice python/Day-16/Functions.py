#Without Function(Performing Addition)
a,b = 10, 20
print("Addition of a and b without using function is: ", a + b)
    
print("="*90)

#With Function(Performing Addition)
def add(x, y):
    return x + y
x,y=map(int, input("Enter two numbers: ").split())
print("Addition of x and y using function is: ", add(x, y))
# A complete function execution tracking.

print("Start-1")

def add(a,b):
    print("Start-3")
    c=a+b
    return c
    print("end-1")

print("Start-2")
result=add(10,20)
print(result)
print("end")
#Bills
def calculate_bill(price, quantity):
    print(price*quantity)
price = int(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
calculate_bill(price, quantity)
#User Defined Function
def Greet1():
    print("Welcome to Functions in Python")
Greet1()

print("="*90)

def Greet(name,age):
    print("Hello",name,"! You are",age,"years old.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
Greet(name,age)
#with arguments and without return value

def add(a,b):
    print("Addition of a and b is: ", a + b)
a,b=map(int, input("Enter two numbers separated by space: ").split())
add(a,b)
#Using the default parameter

def userDetails(name, age=21, city="Hyderabad"):
    print("Hello I am", name, "! I am", age, "years old and I live in", city)

# Calling the function with different combinations of arguments
userDetails("Akshitha")  # Uses default values for age and city
userDetails("Akhil", 25)   # Uses default value for city
userDetails("Pinky", 30, "Bangalore")  # Uses all provided values
# This is an example for keyword only arguments in python. Keyword only arguments are those arguments which can be passed only by keyword and not by position. In python, we can define keyword only arguments by using * in the function definition.
def printDetails(*, name, age, city):
    print("Hello I am", name, "! I am", age, "years old and I live in", city)
printDetails(name="Akshitha",age=21,city="Hyd")
'''printDetails(name = "Akshitha",21,city="Hyd")''' #This raises a type error because it includes a positonal argument too.
def userDetails(name, age, city):
    print("Hello I am", name, "! I am", age, "years old and I live in", city)
userDetails(name="Akshitha", age=21, city="Hyderabad")
#keyword variable-length arguments
def printDetails(**details):
    print("Details of the user are: ", details) #returns the details of the user in dictionary format
    for key, value in details.items():
        print(key, ":", value)

printDetails(name="Akshitha", age=21, city="Hyderabad")
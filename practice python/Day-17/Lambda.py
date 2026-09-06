'''the enclosing scope in the inner function
in the nested function can be made using the 
nonlocal keyword'''
x=100
def Outer():
    x=10
    print("Inside the Outer:",x)
    def Inner():
        nonlocal x
        x=1000
        print("Inside the Inner:",x)
    Inner()
    print("Outside the Inner:",x)
print("start-1")
Outer()
print("Outside the Outer:",x)
num = 10
def Update():
    global num
    num=100
    print("Number inside the function:",num,id(num))
print("Start")
Update() #the function is being called
print("End of the function")
print("Number outside the function:",num,id(num))
#A Global Scope can be accessed
#anywhere within the python code.
company = "Codegnan"
def Display():
    print("Inside Function: ",company)
print("Start-1")
Display()
print("Outside Function: ",company)
print("Start-2")
#Basic Function for squaring a number
def square(x):
    return x * x

print(f"The Square of the number is {square(int(input('Enter a number: ')))}")

print("=" * 100)

# Squaring the number using lambda function
n = int(input("Now Enter another number: "))
sqr = lambda x: x ** 2
print(f"The square of {n} using Lambda function is: {sqr(n)}")
def Student():
    name = "Akshitha"
    print("Inside the function: ",name)
    print("Inside the function: ",name)
Student()
#NON-LOCAL SCOPE IS USED IN NESTED FUNCTIONS 
def Outer():
    def Inner():
        print("Inner Function")
    Inner()
    print("Outer Function")
print("Start")
Outer()
print("End")
def update(items):
    print("Inside the function:",items)
    items.append("Laptop")
cart = ["Mobile", "Watch"]
update(cart)
print("After Updating:",cart)
def update(number):
    number = 100
    print("Inside Function:", number)
value = 50
update(value)
print("Outside Function:", value)
#filtering the even from a list of numbers
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print("The even numbers are:",result)

#filtering odd numbers from a list of numbers
result1 = list(filter(lambda x: x % 2 != 0, numbers))
print("The odd numbers are:",result1)

#Products Above ₹1000
prices = [500, 1200, 800, 2500, 600]
result3 = list(filter(lambda price: price > 1000, prices))
print("The prices that are above 1000 are:",result3)

#Long Usernames
users = ["Akshitha", "codegnan", "admin123", "pinky"]
result4 = list(filter(lambda user: len(user) > 5, users))
print("the long usernames are:",result4)
#squaring numbers of a list
numbers=[1,2,3,4,5,6]
result=list(map(lambda x:x*x, numbers))
print('the square of the numbers of the list:',result)

#Convert Names to Uppercase
names = ["Akshitha", "pinky", "akhil"]
result = list(map(lambda name: name.upper(), names))
print("the uppercase form of the names:",result)

#Calculate String Length
words = ["python", "java", "sql"]
result = list(map(lambda word: len(word), words))
print("the corresponding lengths of the strings are:",result)
#Sum of the numbers of a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, numbers)
print("The sum of the numbers:",result)

#Product of the numbers of a list
numbers = [1, 2, 3, 4]
result = reduce(lambda a, b: a * b, numbers)
print("The product of the numbers:",result)

#Largest Number
numbers = [10, 25, 8, 40, 15]
result = reduce(lambda a, b: a if a > b else b, numbers)
print("The largest number is:",result)
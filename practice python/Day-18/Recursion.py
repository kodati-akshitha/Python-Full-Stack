def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

if __name__=="__main__":
    n=int(input("Enter a number:"))
    print(fact(n))
def Fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return Fibo(n-2)+Fibo(n-1)

if __name__=="__main__":
    n = int(input("enter a number: "))
    result=Fibo(n)
    print(f"The {n+1}th fibonacci number is {result}")
    print(f"The Fibonacci series upto {n} is",end=" ")
    for i in range(n):
        print(Fibo(i),end=" ")
def sum_natural(n):
    if n==1:
        return 1
    return n+sum_natural(n-1)

if __name__=="__main__":
    n = int(input("enter a number:"))
    result=sum_natural(n)
    print(f"The sum of first {n} natural numbers is {result}")

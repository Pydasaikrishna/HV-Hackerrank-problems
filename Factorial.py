def factorial(x):
    if (x==1):
        return 1
    else:
        return(x*factorial(x-1))

z = int(input("Enter a Number: "))
print("The factorial of ",z,"is",factorial(z))
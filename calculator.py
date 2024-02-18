import math as m

def add(a,b):
    print(a, " + " , b ," = ", (a+b))

def sub(a,b):
    print(a, " - " , b ," = ", (a-b))

def mul(a,b):
    print(a, " * " , b ," = ", (a*b))

def div(a,b):
    if(a==0):
        print("Dividend cannot be zero")
    elif(b==0):
        print("Divisor cannot be zero")
    else:
        print(a, " / " , b ," = ", (a/b))

def mod(a,b):
    print(a, " % " , b ," = ", (a%b))


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Operations List \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulous \n")

choice = int(input("Enter your choice : "))

def check (choice): 
    match choice:
        case 1:
            add(a,b)
        case 2:
            sub(a,b)
        case 3:
            mul(a,b)
        case 4:
            div(a,b)
        case 5:
            mod(a,b)
        case _:
            print("Enter a valid option")

check(choice)

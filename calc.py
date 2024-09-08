print("###  1-addition ###\n###  2-substitutuin ###\n###  3-multiplication ###\n###  4-over ###\n")
choice = int(input("choose ur operation: "))
a = int(input("enter a: "))
b = int(input("enter b: "))

def addition(x,y):
    return x + y

def substution(x,y):
    return x - y

def multiply(x,y):
    return x * y

def over(x,y):
    return x / y

if choice == 1:
   print(addition(a, b))
if choice == 2:
   print(substution(a, b))
if choice == 3:
   print(multiply(a, b))
if choice == 4:
   print(over(a, b))

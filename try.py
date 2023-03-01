print ("select an operation to perform")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

operation=input()


if operation=="1":
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    c=a+b
    print(c)
elif operation == "2":
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    c=a-b
    print(c)
elif operation=="3":
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    c=a*b
    print(c)
elif operation=="4":
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    c=a/b
    print(c)
    if c==0:
        print("division by zero")

else:

    print("invalid operation")

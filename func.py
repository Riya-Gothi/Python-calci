def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x/y)
no1=eval(input("enter number1"))
no2=eval(input("enter number2"))

print("select the operation from the below")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

while(True):    
    choice=int(input("select the opertaion"))
    if choice in(1,2,3,4,5):
        if choice==1:
            print(add(no1,no2))
        elif choice==2:
            print(subtract(no1,no2))
        elif choice==3:
            print(multiply(no1,no2))
        elif choice==4:
            print(divide(no1,no2))
        elif choice==5:
            exit() 
        else:
            print("invalid operation")



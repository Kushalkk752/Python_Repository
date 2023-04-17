def add(x, y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("select operation")
print("1:add \n 2:sub \n 3:mul \n 4:div \n")
choice = int(input("enter your choice 1/2/3/4"))
n1 = int(input("enter the number 1"))
n2 = int(input("enter the number 2"))
if(choice == 1):
    print(f"{n1} + {n2} = {add(n1,n2)}")

elif(choice == 2):
    print(f"{n1} - {n2} = {sub(n1,n2)}")

elif(choice == 3):
    print(f"{n1} * {n2} = {mul(n1,n2)}")        

elif(choice == 4):
    print(f"{n1} / {n2} = {div(n1,n2)}") 

else:
    print("Invalid input")       
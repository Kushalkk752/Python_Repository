a = int(input("enter the value of a \n"))
b = int(input("enter the value of b \n"))
c = int(input("enter the value of c \n"))
#Calculate the semi-perimeter
s = (a+b+c)/2

#Calculate the area 
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"The area of the triangle is {area}")
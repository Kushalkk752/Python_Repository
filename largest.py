#largest among the three numbers
num1 = int(input("enter the number1 "))
num2 = int(input("enter the number2 "))
num3 = int(input("enter the number3 "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1

elif (num2 >=  num3) and (num2 >= num1):
    largest = num2 

else:
    largest = num3

print(f"The largest among the three numbers {num1}, {num2}, {num3} is {largest}")        



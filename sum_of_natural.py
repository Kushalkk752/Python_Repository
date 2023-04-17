num = 16 

if num < 0:
    print("enter a positive number")

else:
    sum = 0
    temp = num

    while temp > 0:
        sum += temp 
        temp -= 1   

    print(f"sum of {num} natural number is {sum}")   


num2 = int(input("enter the number for which the sum has to be calculated: "))
sum = num2*(num + 1)/2 
print(f"sum of {num2} natural numbers is {sum}")    
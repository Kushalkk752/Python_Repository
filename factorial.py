num = 7
factorial = 1

if num < 0:
    print("factorial of number is not possible for a negative number")

elif num == 0:
    print("the factorial of 0 is 1")

else:
    for i in range(1, num+1):
        factorial = factorial*i

    print(f"The factorial of number {num} is {factorial}")   
    
             
    
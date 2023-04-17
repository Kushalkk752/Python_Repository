def computeLCM(x,y):
    if(x>y):
        largest = x

    else:
        largest = y

    while(True):
        if(largest % x == 0)and (largest % y == 0):
            lcm = largest 
            break

        largest += 1

    return lcm 

num1 = 54
num2 = 24
print(f"The lcm of {num1} and {num2} is {computeLCM(num1,num2)}")

terms = 8
n1 = 0
n2 = 1
count = 0
if terms <= 0:
    print("fibonacci series for negative number is not possible")

elif terms == 0:
    print(f"fibonacci series is {n1}")

else:
    print(f"Fibonacci series upto {terms} is : ")
    
    while count < terms:
        print(n1, end = " , ")
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count+=1

print()        

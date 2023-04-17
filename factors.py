def print_factors(x):
    print(f"The factors of {x} are: ")

    for i in range(1,x+1):
        if(x%i == 0):
            print(i,end = " ")

num = 235
print_factors(num)          
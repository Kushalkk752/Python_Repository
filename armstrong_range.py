lower = 100
upper = 2000
for num in range(lower, upper+1):
    sum = 0
    order = len(str(num))
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp = temp//10

    if sum == num:
        print(f"{sum}",end=", ")

print()             
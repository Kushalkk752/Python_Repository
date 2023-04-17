num = 153
sum = 0
order = len(str(num))
temp = num 
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //=10

if num == sum:
    print(f"{num} is a armstrong number")    
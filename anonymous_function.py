terms = 10
result = list(map(lambda x: 2**x, range(terms)))
print(f"the total number of terms is {terms}")
for i in range(terms):
    print(f"2 raised to power of {i} is {result[i]}")
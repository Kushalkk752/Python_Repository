import cmath
#co-efficients of a mathematical equation
a = 1
b = 5
c = 6

#calculate the discriminant
d = (b**2) - (4*a*c)

#find the two solutions
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print(f"the roots are {root1} {root2}")
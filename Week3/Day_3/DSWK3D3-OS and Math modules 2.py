import math

#Square root
print(math.sqrt(25))

#Rounding to ceiling and floor
print(math.floor(9.7))
print(math.ceil(9.5))

#Factorial
print(math.factorial(5))

#EXAMPLE
print ("EXAMPLES:")
numbers=[20,22,24,26,28,30]
for n in numbers:
    print(math.sqrt(n))
    print(math.ceil(n+ 0.2))
    print(math.floor(n-0.7))
    print(math.factorial(n))
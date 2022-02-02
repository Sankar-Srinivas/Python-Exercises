# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence

from math import *
c = 50
h = 30
value = []
D=input('Enter numbers')
items=D.split(",")

for i in items:
    value.append(str(int(sqrt(2*c*int(i)/h))))

print (','.join(value))

# Using Map and a function
def calc(j):
    return str(int(sqrt((2*c*int(j))/h)))


print(','.join((map(calc,items))))


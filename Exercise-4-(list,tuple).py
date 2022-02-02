# Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.

n=input('Enter numbers')
list=n.split(",")
tup=tuple(list)

print(list)
print(tup)
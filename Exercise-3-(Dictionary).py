#With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

# Method-1
n=int(input('enter a number'))

c=dict()
for i in range(1,n+1):
    c[i]=(i*i)
print(c)

# Method-2
ans={i:i*i for i in range(1,n+1)}
print(ans)

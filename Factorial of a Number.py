# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# Method-1(using for loop)
n=int(input('please enter the number for which you want to find factorial'))
fact=1
for i in range(1,n+1):
    fact=fact*i

print(fact)

#Method-2(use functions)-Recursive Method
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(n))



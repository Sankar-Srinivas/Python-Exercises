# Define a class which has at least two methods:
#
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class Car:
    def __init__(self,x):
        self.x=x

    def get_string(self):
        print(self.x)

    def Upper(self):
        print(self.x.upper())

a=Car('sankar')
a.get_string()
a.Upper()
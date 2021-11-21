'''
Ask the user for a number and determine whether the number is prime or not.

'''
import sys

def get_integer(help_text="Give a number: "):

    return int(input(help_text))

num = get_integer()

for i in range(2,num-1):
    if (num%i)==0:
        sys.exit("The number is not prime")

print("Number is prime")

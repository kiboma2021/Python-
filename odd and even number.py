'''
Ask the user for a number. Depending on whether the number is even or odd, print out an 
appropriate message to the user. Hint: how does an even / odd number react differently 
when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number 
    to divide by (check). If check divides evenly into num, tell that to the user. 
    If not, print a different appropriate message.

'''

x=int(input("Enter a number:"))

if (x%2)==0:
    if (x%4)==0:
        print(str(x) +" is an even number and divisible by 4")
    else:
        print(str(x) +" is an even number and not divisible by 4")
else:
    print(str(x)+" is an odd number")
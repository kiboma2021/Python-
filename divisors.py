'''
Create a program that asks the user for a number and then prints 
out a list of all the divisors of that number.
'''

num=int(input("Insert a number: "))
x=[]
for i in range(1,num):
    if (num%i)==0:
        x.append(i)
print(x)


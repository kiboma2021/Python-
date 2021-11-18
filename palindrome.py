'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)

'''

string=input("Inert a string: ")

if(string==string[::-1]):
   print("Palindrome")

else:
   print("Not palindrome")
   




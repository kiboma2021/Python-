# Python-
Python exercises

1. Create a program that asks the user to enter their name and their age. Print out a message 
addressed to them that tells them the year that they will turn 100 years old.

Solution:

    from datetime import date

    name=input("What is your name: ")
    age=int(input("What is your current age: "))
    turn100years=str(date.today().year+100-age)

    print("Hello "+name +",you will be 100 years old in "+turn100years)


2. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. If the number is a multiple of 4, print out a different message.

Solution:

    x=int(input("Enter a number:"))

    if (x%2)==0:
        if (x%4)==0:
            print(str(x) +" is an even number and divisible by 4")
        else:
            print(str(x) +" is an even number and not divisible by 4")
    else:
        print(str(x)+" is an odd number")


3. Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Solution:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    x=[] #holds empty list

    for i in a:
        if i<5:
            print(i), # prints one by one
            x.append(i)  # Adding objects to x
    print(x) # prints in one line


4. Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

Solution:

    num=int(input("Insert a number: "))
    x=[]
    for i in range(1,num):
        if (num%i)==0:
            x.append(i)
    print(x)


5. Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Solution:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,55]

    x=[]
    n=0
    for i in a:
        for j in b:
            if i==j:
                x.append(i)

    y=[]
    for i in x:
        if i not in y:
            y.append(i)

    print(y)


6. Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

Solution:

    string=input("Inert a string: ")

    if(string==string[::-1]):
      print("Palindrome")

    else:
      print("Not palindrome")


7. Let’s say I give you a list saved in a variable: 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

Solution:

    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    newlist=[]
    for i in a:
        if (i%2)==0:
            newlist.append(i)

    print(newlist)



8. Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors,
Scissors beats paper,
Paper beats rock,


Solution:

    import sys

    user1 = input("What's your name?")
    user2 = input("And your name?")
    user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
    user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

    def compare(u1, u2):
        if u1 == u2:
            return("It's a tie!")
        elif u1 == 'rock':
            if u2 == 'scissors':
                return("Rock wins!")
            else:
                return("Paper wins!")
        elif u1 == 'scissors':
            if u2 == 'paper':
                return("Scissors win!")
            else:
                return("Rock wins!")
        elif u1 == 'paper':
            if u2 == 'rock':
                return("Paper wins!")
            else:
                return("Scissors win!")
        else:
            return("Invalid input! You have not entered rock, paper or scissors, try again.")
            sys.exit()

    print(compare(user1_answer, user2_answer))
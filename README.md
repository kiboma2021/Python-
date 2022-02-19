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

9. Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.


solution:

    import random
    
    #random.randrange(begin, end, step counter)

    #randint() function is somewhat similar to the randrange()

    #Randint() has two mandatory arguments: start and stop

    #It has an inclusive range, i.e., can return both endpoints as the random output.

    #random.random()- Generate random float number between 0 and 1

    #Seed() to repeat a random number


    #print("First Random Number: ", random.randrange(0, 100, 1)) #excludes zero and 100

    #print("second Random Number: ", random.randrange(0, 100)) #includes zero and 100

    #print("Third Random Number: ", random.random()) #radom number between 0 and 1

    #random.seed(4)
    #print("Generate Fourth Random Number: ", random.random())
    #random.seed(5)
    #print("Repeat Fourth Random Number: ", random.random())

    #print("Generate fifth Random Float Number: ", random.uniform(10, 100))
    #print("Generate sixth Random Float Number: ", random.uniform(10, 100))

    x=random.randint(1,9)
    userinput=input("Guess a number between 1-9:")

    a=0
    b=0
    c=0

    while userinput !='exit':

        userinput=int(userinput)
        if userinput>1 and userinput<=9:
            print("random number is", x)
                
            if x==userinput:
                print("Your guess is correct")
                a=a+1

            elif x<userinput:
                print("Your guess is too high")
                b=b+1
            else:
                print("Your guess is too low")
                b=b+1

        else:
            print("incorrect input")
            c=c+1

        x=random.randint(1,9)
        userinput=input("Guess a number between 1-9:")

    print("Number of correct attempts:", a)
    print("Number of incorrect attemts:", b)
    print("Number of incorrect inputs:", c)

10. Ask the user for a number and determine whether the number is prime or not.

solution:

    import sys
    def get_integer(help_text="Give a number: "):

        return int(input(help_text))

    num = get_integer()

    for i in range(2,num-1):
        if (num%i)==0:
            sys.exit("The number is not prime")

    print("Number is prime")

11. Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. Write this code inside a function.    

solution:

    def list_fe(a):
        return[a[0],a[len(a)-1] ]

12. Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

solution:

    def fibonacci():
        num = int(input("How many fibonnaci numbers do you want to generate?:  "))
        i = 1
        if num == 0:
            fib = []
        elif num == 1:
            fib = [1]
        elif num == 2:
            fib = [1,1]
        elif num > 2:
            fib = [1,1]
            while i < (num - 1):
                fib.append(fib[i] + fib[i-1])
                i += 1
        return fib
    print(fibonacci())
    input()

13. Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.


14. Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

    if __name__ == '__main__':
        
        n = int(input().strip())

        if n%2!=0:
            print("Weird")
        if n%2==0 and n>=2 and n<=5:
            print("Not Weird")
        if n%2==0 and n>=6 and n<=20:
            print("Weird")
        if n%2==0 and n>20:
            print("Not Weird")
        
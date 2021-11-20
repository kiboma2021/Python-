'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the players 
want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

'''

import sys

user1 = input("Player 1 name?")
user2 = input("Player 2 name?")
user1_answer = input("%s, do yo want to choose 1=rock, 2=paper or 3=scissors?" % user1)
user2_answer = input("%s, do you want to choose 1=rock, 2=paper or 3=scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == '1':
        if u2 == '3':
            return(user1 + " wins!")
        else:
            return(user2 + " wins!")
    elif u1 == '3':
        if u2 == '2':
            return(user1 + " wins!")
        else:
            return(user2 + " wins!")
    elif u1 == '2':
        if u2 == '1':
            return(user1 + " wins!")
        else:
            return(user2 + " wins!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))


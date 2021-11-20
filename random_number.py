'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

'''
import random

print("First Random Number: ", random.randrange(0, 100, 1)) #excludes zero and 100

print("second Random Number: ", random.randrange(0, 100)) #includes zero and 100

print("Third Random Number: ", random.random()) #radom number between 0 and 1

random.seed(4)
print("Generate Fourth Random Number: ", random.random())
random.seed(5)
print("Repeat Fourth Random Number: ", random.random())

print("Generate fifth Random Float Number: ", random.uniform(10, 100))
print("Generate sixth Random Float Number: ", random.uniform(10, 100))

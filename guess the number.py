#Guess the number, my version
import random
number = random.randint(1,20)
guesses = 0
myName = input("Hello, what is your name? ")
print("Well, " +myName + " I am thinking of a number between 1 and 20.")

for guesses in range(6):
    guesses = guesses+1
    myNumber = int(input("Take a guess.\n"))
    if myNumber == number:
        print("Good job, " +myName+ "! You guessed the number in: " + str(guesses)+ " times!")
        break
    if myNumber < number:
        print("Your guess is too low.")
    if myNumber > number:
        print("Your guess is too high.")
if myNumber != number:
    print("Nope. The number I was thinking of was " + str(number) + ".")

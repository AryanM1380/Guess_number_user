import random

def guess_number():
       low = 1
       high = 100
       secret_number = random.randint(low, high)
       guess = None
       print("Welcome to the Guess the Number game!")
       print("Think of a number between 1 and 100 and I'll try to guess it.")

       while guess != secret_number:
              guess = random.randint(low, high)
              print("I guess:", guess)
              if guess > secret_number:
                     print("Too high! I'll guess lower.")
                     high = guess - 1
              elif guess < secret_number:
                     print("Too low! I'll guess higher.")
                     low = guess + 1
       print("I guessed it! The secret number is", secret_number)

guess_number()

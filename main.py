# This is my Guess Number game in Python.
# The computer will generate a random number
# The user will choose an integer number
# The computer will tell if the number guessed was too high or too low
# The computer will show how many tries were needed to guess the right number
import random

secret_number = random.randint(1, 100)
guess_number = 0
aux = 0
while guess_number != secret_number:
    guess_number = int(input('Choose a number between 1 and 100: '))
    aux = aux + 1
    if guess_number > secret_number:
        print('Your number was too high.')
    elif guess_number < secret_number:
        print('your number was too low.')
    else:
        print(f'Congratulations! The secret number is {secret_number} '
              f'and you got in {aux} tries.')

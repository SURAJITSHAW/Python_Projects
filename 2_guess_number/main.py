import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 & {x}: '))
        print(f'Your number is: {guess}')
        print(f'Computer generated random number is: {random_number}')
        print(f'Let\'s give it a another try!')
    print(f'Wooohoooooo!!! You guessed it correctly.')

guess(10)
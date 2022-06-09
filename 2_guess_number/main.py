import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 & {x}: '))
        if guess < random_number:
            print('Your guess is too low.')
        else :
            print('Your guess is too high.')
        print(f'Let\'s give it a another try!')
        
    print(f'Wooohoooooo!!! You guessed it correctly.')

guess(10)
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

# guess(10)

def computer_guess(x):
    print(f'Choose a number between 1 & {x} in your mind,\n and now I\'m gonna guess which number did you choose :)')
    print()
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C) ?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number, {guess} correctly!')


computer_guess(10)
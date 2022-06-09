import random

def play():
    user = input("What is your choice? 'r' for Rock, 'p' for Paper, & 's' for Secissor :\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie!'

    if Is_win(user, computer):
        return 'You won :)'
    return 'You Lost :('

# return True if player(first argument) wins
def Is_win(player, opponent):
    # p > r, r > s, s > p
    if (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p'):
        return True 

print(play())
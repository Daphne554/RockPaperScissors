import random

def play():
    user = input("Type rock/paper/scissors: ").lower()
    computer = random.choice(["rock", "paper", "scissors"])

    if user == computer:
        return "Its a tie"

    if is_win(user,computer):
        return "You win"

    return "You lose"

def is_win(player, opponent):
    if (player == "rock" and opponent == "scissors") or (player == "scissors" and opponent =="paper")\
            or (player =="paper "and opponent == "rock"):
        return True

print(play())
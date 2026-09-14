import random

while True:
    choices = ["rock", "scissors", "paper"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock,scissors,paper?: ").lower()
    if computer == player:
        print("computer: " + computer)
        print("player: " + player)
        print("ping")
    elif computer == "rock":
        if player == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("You win!")
        if player == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("You lose!")
    elif computer == "paper":
        if player == "scissors":
            print("computer: " + computer)
            print("player: " + player)
            print("You win!")
        if player == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("You lose!")
    elif computer == "scissors":
        if player == "rock":
            print("computer: " + computer)
            print("player: " + player)
            print("You win!")
        if player == "paper":
            print("computer: " + computer)
            print("player: " + player)
            print("You lose!")
    play_again = input("play again?: (yes/no)")
    if play_again != "yes":

        break
print("bye")

import random
while True:
    choices = ["rock", "paper", "scissor"]
    computer =random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper or scissor? :").lower()
        print("computer: ", computer)
        print('player: ',player)

    if player == computer:
        print("Tie")
    elif player == "rock":
        if computer == "scissor":
            print("Player win !")
        else:
            print("Player lost !")
    elif player == "paper":
        if computer == "scissor":
            print("Player lose !")
        else:
            print("Player win !")
    elif player == "scissor":
        if computer == "rock":
            print("Player lose !")
        else:
            print("Player win !")
    play_again = input("Wanna play again ? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Game over")
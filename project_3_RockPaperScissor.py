import random

def game():
    computer = ["rock", "paper", "scissor"]

    comp_player = random.choice(computer)
    # print(comp_player)
    player_2 = int(input(" for rock-press 1, for paper-press 2, for scissors-press 3 \n" ))

    if comp_player == "rock" and player_2 == 1 or comp_player =="paper" and player_2 ==2\
    or comp_player =="scissor" and player_2 ==3:
            print("match draw")
    elif comp_player == "rock" and player_2 == 3 or \
            comp_player == "paper" and player_2 == 1 or \
            comp_player == "scissor"  and player_2 == 2:
            print("Computer win ")
    elif player_2 >3:
            print("enter a valid number")
    else:
            print("You Win! Congrats")      

game()
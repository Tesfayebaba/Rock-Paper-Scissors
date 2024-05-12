# Version 0.3 [Rock,Paper,Scissors]

import random
import keyboard

Game_mode = input("Select game mode:\n 1.) Singleplayer \n 2.) Multiplayer  \n")
Choices = ["rock", "paper", "scissors"]
Player = ["Player 1", "Player 2"]



def singlePlayer():

    print("Make a throw!!!")
    player1_choice = input(" Type rock, paper or scissors: \n")

    def rockAlgorithm():
        if player1_choice == "rock" and player2_choice == "rock" in Choices:
            print("It's a draw!!!")
        elif player1_choice == "rock" and player2_choice == "paper" in Choices:
            print(f'"{player2_choice}" Computer Won!!!')
        elif player1_choice == "rock" and player2_choice == "scissors" in Choices:
            print(f'"{player1_choice}" You Win!!!')
        else:
            pass

    def papersAlgorithm():
        if player1_choice == "paper" and player2_choice == "paper" in Choices:
            print("It's a draw!!!")
        elif player1_choice == "paper" and player2_choice == "rock" in Choices:
            print(f'"{player1_choice}" You Win!!!')
        elif player1_choice == "paper" and player2_choice == "scissors" in Choices:
            print(f'"{player2_choice}" Computer Won!!!')
        else:
            pass

    def scissorAlgorithm():
        if player1_choice == "scissors" and player2_choice == "scissors" in Choices:
            print("It's a draw!!!")
        elif player1_choice == "scissors" and player2_choice == "rock" in Choices:
            print(f'"{player2_choice}" Computer Won!!!')
        elif player1_choice == "scissors" and player2_choice == "paper" in Choices:
            print(f'"{player1_choice}" You Win!!!')
        else:
            pass



    if player1_choice in Choices:
        player2_choice = random.choice(Choices)

        print(f'You picked {player1_choice} & Computer picked {player2_choice}')
        rockAlgorithm()
        scissorAlgorithm()
        papersAlgorithm()
    else:
        print("Invalid Option")

def multiPlayer():

    player1_choice = random.choice(Choices)
    player2_choice = random.choice(Choices)

    def rockAlgorithm():
        if player1_choice == "rock" and player2_choice == "rock" in Choices:
            print("It's a draw!!!")
        elif player1_choice == "rock" and player2_choice == "paper" in Choices:
            print(f'Player 2 wins!!! "{player2_choice}"')
        elif player1_choice == "rock" and player2_choice == "scissors" in Choices:
            print(f' Player 1 wins!!! "{player1_choice}" ')
        else:
            pass

    def papersAlgorithm():
        if player1_choice == "paper" and player2_choice == "paper" in Choices:
            print("It's a draw!!!")
        elif player1_choice == "paper" and player2_choice == "rock" in Choices:
            print(f'Player 2 wins!!! "{player2_choice}" ')
        elif player1_choice == "paper" and player2_choice == "scissors" in Choices:
            print(f' Player 2 wins!!! "{player2_choice}" ')
        else:
            pass

    def scissorAlgorithm():
        if player1_choice == "scissors" and player2_choice == "scissors" in Choices:
            print("It's a draw!!!")
        elif player1_choice == "scissors" and player2_choice == "rock" in Choices:
            print(f' Player 2 wins!!! "{player2_choice}" ')
        elif player1_choice == "scissors" and player2_choice == "paper" in Choices:
            print(f'Player 1 wins!!!  "{player1_choice}" ')
        else:
            pass
    #

    # def result():
    #
    #     if player1_choice and player2_choice in Choices:
    #
    #         print(f'You picked {player1_choice} & Computer picked {player2_choice}')
    #         rockAlgorithm()
    #         scissorAlgorithm()
    #         papersAlgorithm()
    #
    #     else:
    #         print("Invalid Option")
    if player1_choice and player2_choice in Choices:

        print(f'You picked {player1_choice} & Computer picked {player2_choice}')
        rockAlgorithm()
        scissorAlgorithm()
        papersAlgorithm()

    else:
        print("Invalid Option")

def random_player():

    print(f'You are {random.choice(Player)}')

if Game_mode == "1":
    singlePlayer()

elif Game_mode == "2":
    while True:
        print("Press spacebar on your keyboard when ready!!!")
            # if random_player() == Player:

        if keyboard.is_pressed("space"):
                multiPlayer()
                break

else:
    pass


# # print("Press spacebar to get player no. ")
    # if keyboard.is_pressed("space"):
    #     random_player()




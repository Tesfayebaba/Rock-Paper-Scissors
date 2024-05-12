import random
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
            print(f'"{player2_choice}" Computer Won!!!')
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

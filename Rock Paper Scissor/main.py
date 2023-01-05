# Simple starter project
import random 
 
#Create a list of option options 
option = ["Rock", "Paper", "Scissors"]

#Assign the computer a random option
computer_action = option[random.randint(0,2)] 
 
# Variables
player = False


while player == False: 
#Set the player to True 
    print("|Rock, Paper and Scissors|")
    player = input("\n(Rock), (Paper) or (Scissors)?: ").capitalize()
    if player == computer_action: 
        print("Computer chooses", computer_action)
        print("(Tie!)") 
    elif player == "Rock": 
        if computer_action == "Paper": 
            print("Computer chooses", computer_action)
            print("(You lose!)") 
        else: 
            print("Computer chooses", computer_action)
            print("(You win!)") 
    elif player == "Paper": 
            if computer_action == "Scissors" or "Scissor":
            print("Computer chooses", computer_action)
            print("You lose!") 
        else: 
            print("Computer chooses", computer_action)
            print("(You win!)") 
    elif player == "Scissors": 
        if computer_action == "Rock": 
            print("Computer chooses", computer_action)
            print("(You lose)") 
        else: 
            print("Computer chooses", computer_action)
            print("(You win!)") 
    else: 
        print("Invalid option, please try again") 
    # Set player to False to continue loop
    player = False 
    # Assign computer with a new action
    computer_action = option[random.randint(0,2)]  

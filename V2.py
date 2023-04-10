import random
import sys

CHOICES = ["rock","paper","scissors"]

def check_if_tie(player:str,computer:str) -> bool:
    """
    This function checks if the player and computer has chosen the same string value.
    Returns True if its a tie
    Returns False if its NOT a tie
    """
    # if player == computer:
    #     return True
    # else:
    #     return False
    return player == computer

def compare(player:str,computer:str) -> bool:
    """
    This function takes 2 arguments that should be the litteral strings and returns a boolean wether the player wins
    """
    match player:
        case "rock":
            match computer:
                case "paper":
                    return False
                case "scissors":
                    return True
        case "paper":
            match computer:
                case "scissors":
                    return False
                case "rock":
                    return True
        case "scissors":
            match computer:
                case "rock":
                    return False
                case "paper":
                    return True

def play_again():
    play_again = input("Play again?(yes/no): ").lower()
    if play_again == "yes":
       return True
    else:
        print("Thank you for playing, bye!")
        sys.exit(0)

def validate_user_input(input:str) -> bool:
    if input in CHOICES:
        return True
    else:
        print(f"Invalid input, please choose from this list:\n {CHOICES}")
        return False

while True:
    computer = random.choice(CHOICES)                        #We define a variable called computer, that uses the random module to choose a string from the choices variable
    player = None                                            #We define a variable called player, that will be used to house the choice that the player will make.
    valid_input = False

    while not valid_input:                             #While the player has NOT choosen an option defined in the choices list
        player = input("Rock, paper or scissors?: ").lower() #Request input from player, and put input in lowercase(to adhere to case sensitive input).
        valid_input = validate_user_input(player)

    print(f"Computer has chosen: {computer}, You choose {player}")

    if check_if_tie(player,computer):
        print("Its a tie!")
        if play_again():
            continue

    player_wins = compare(player,computer)
    if player_wins:
        print("YOU WIN!")
    else:
        print("You lose!")
    if play_again():
        continue
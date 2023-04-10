#Time to make a game! A very simple one atleast, using the random module!

import random                               #Import Python built in module "Random"
#In order to make the game replayable, the entire script will have to be indented in a while loop

while True:
    choices = ["rock","paper","scissors"]       #we define a variable with a list of 3 strings
    computer = random.choice(choices)           #We define a variable called computer, that uses the random module to choose a string from the choices variable
    player = None                               #We define a variable called player, that will be used to house the choice that the player will make.

#At this point, computer has already chosen between rock, paper or scissors, through random.choice(choices)
#To make sure the player adheres to the game, we have to make sure they pick between rock, paper or scissors.
#And dont do something stupid like picking "bazooka" or something.
#To do this we use a while loop.

    while player not in choices:                             #While the player has NOT choosen an option defined in the choices list
        player = input("Rock, paper or scissors?: ").lower() #Request input from player, and put input in lowercase(to adhere to case sensitive input).

#Now to define the win conditions.
#First we will check if we encounter a tie.
    if player == computer:              #If the player variable equals the computer variable(They have chosen the same value) then:
        print("computer: ",computer)    #Print the choice of the computer
        print("player: ",player)        #print the choice of the player
        print("Its a tie!")             #print that its a tie!

#Now to define every possible win condition!
#We use elif statements for each of the players possible inputs, and 2 if statements indented depending on what possible choice the computer made.
#Remember that its only 2, because the 3rd is a tie, which we already defined above for all 3 choices.
#First, if the player chooses rock:
    elif player == "rock":              #Otherwise, if the player variable equals rock
        #lose condition
        if computer == "paper":             #and the computer variable equals paper
            print("computer: ", computer)   # Print the choice of the computer
            print("player: ", player)       # print the choice of the player
            print("You loose!")             # print that its a loss!
        #win condition
        if computer == "scissors":          #and the computer variable equals scissors
            print("computer: ", computer)   # Print the choice of the computer
            print("player: ", player)       # print the choice of the player
            print("You loose!")             # print that its a win!

#Second, if the player chooses paper(litterally copy paste with corrections):
    elif player == "paper":              #Otherwise, if the player variable equals paper
        #lose condition
        if computer == "rock":             #and the computer variable equals rock
            print("computer: ", computer)   # Print the choice of the computer
            print("player: ", player)       # print the choice of the player
            print("You loose!")             # print that its a loss!
        #win condition
        if computer == "scissors":          #and the computer variable equals paper
            print("computer: ", computer)   # Print the choice of the computer
            print("player: ", player)       # print the choice of the player
            print("You loose!")             # print that its a win!

#And again, for scissors
    elif player == "scissors":              #Otherwise, if the player variable equals scissors
        #Lose condition
        if computer == "rock":             #and the computer variable equals rock
            print("computer: ", computer)   # Print the choice of the computer
            print("player: ", player)       # print the choice of the player
            print("You loose!")             # print that its a loss!
        #win condition
        if computer == "paper":          #and the computer variable equals paper
            print("computer: ", computer)   # Print the choice of the computer
            print("player: ", player)       # print the choice of the player
            print("You loose!")             # print that its a win!
    #Then we end the indentation tying the whole game code to the first while loop to see if we play again.
    #If the player choose yes, the game will start over.
    play_again = input("Play again? (yes/no): ").lower() #define variable play_again as user input in lowercase
    #if the player choose anything BUT yes, the game will end
    if play_again != "yes":    #If user input does NOT equal to "yes"
        break                  #end program
print("Bye!")                  #Finish with a nice goodbye!




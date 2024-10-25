import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    Converts name to number.
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Error: Unknown name", name)
        return None

def number_to_name(number):
    """
    Converts number to name.
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Error: Unknown number", number)
        return None

def rpsls(player_choice): 
    """ 
    Play a round of Rock-paper-scissors-lizard-Spock.
    player_choice: the name of the player's choice
    """
    print("\n")  # Blank line to separate consecutive games
    
    print("Player chooses", player_choice)
    
    # Convert player_choice to player_number
    player_number = name_to_number(player_choice)
    if player_number is None:
        return  # Exit if there was an error in player input
    
    # Generate random choice for the computer
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses", comp_choice)
    
    # Compute the difference modulo 5
    diff = (comp_number - player_number) % 5
    
    # Determine the winner
    if diff == 1 or diff == 2:
        print("Computer wins!")
    elif diff == 3 or diff == 4:
        print("Player wins!")
    else:
        print("Player and computer tie!")
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

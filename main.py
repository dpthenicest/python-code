import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choices = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choices}
    return choices 

# print(choices)

# dict = {"name": "baeu", "color": choices}

# food = ["pizza", "carrots", "ice cream"]
# dinner = random.choice(food)
# ran_number = random.choice(range(1, 11))
# ran_choice = random.randint(1, 10)

# print(f"Random dinner: {dinner}, random number: {ran_number}")

def check_win(player, computer):
    print(f"You chose player: {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)

import random

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ")
    if user_input.lower() == "rock":
        return "rock"
    elif user_input.lower() == "paper":
        return "paper"
    elif user_input.lower() == "scissors":
        return "scissors"
    else:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return get_user_choice()

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("User wins!")
    else:
        print("Computer wins!")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        print(f"User score: {user_score}")
        print(f"Computer score: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
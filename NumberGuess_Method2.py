from art import logo
import random

def display_welcome():
    print(logo)
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100")

def get_difficulty():
    while True:
        mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if mode.lower() in ["easy", "hard"]:
            return mode.lower()
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")

def get_user_guess():
    while True:
        try:
            return int(input("\nMake a guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, answer):
    if guess < answer:
        print("Too low, try again.")
        return False
    elif guess > answer:
        print("Too high, try again.")
        return False
    else:
        return True

def play_game():
    display_welcome()
    randNum = random.randint(0, 100)
    mode = get_difficulty()
    max_attempts = 10 if mode == "easy" else 5
    attempt_count = 0

    is_game_over = False
    while not is_game_over and attempt_count < max_attempts:
        user_num = get_user_guess()
        attempt_count += 1
        if check_guess(user_num, randNum):
            print(f"You got it! The number was {randNum}. Congratulation!")
            is_game_over = True

    if not is_game_over:
        print(f"Too many attempts. The number was {randNum}. Game over!")

play_game()

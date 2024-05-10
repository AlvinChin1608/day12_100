#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

def play_game():
  print(logo)
  
  randNum = random.randint(0,100)
  attempt_count = 0
  guesses = 0
  
  print("Welcome to the Number Guessing Game!\n")
  print("I'm thinking of a number between 1 and 100")
  print(f"The number is {randNum}")
  
  mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if mode == "easy":
    max_attempts = 10
  elif mode == "hard":
    max_attempts = 5
  else:
    print("Invalid difficulty level. Defaulting to easy mode")
    max_attempts = 10
    
  
  is_game_over = False
  while not is_game_over:
    if attempt_count < max_attempts:
      user_num = int(input("\n\nMake a guess: "))
      if user_num != randNum:

        if user_num < randNum:
          print("\n\nToo low, try again")
          attempt_count += 1
          print(f"Here is your remaining attempts left {max_attempts-attempt_count}")
        elif user_num > randNum:
          print("\n\nToo high, try again")
          attempt_count += 1
          print(f"Here is your remaining attempts left {max_attempts-attempt_count}")
      else:
        print("You got it! Congratulation")
        is_game_over = True
    else:
      print("Too many attempts. Game Over!!!")
      is_game_over = True
      
play_game()

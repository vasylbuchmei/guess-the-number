
from art import logo
import random

def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level=="easy":
    return 10
  elif level == "hard":
    return 5 

def checking(guessed_number,answer,turns):
  if guessed_number > answer:
    print("Too high")
    return turns - 1
  elif guessed_number < answer:
    print("Too low")
    return turns -1
  else:
    print(f"You win. The answer was {answer}")

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("Guess a number between 1 and 100.")
  answer = random.choice(range(1,101))

  turns = difficulty()
  #Repeat the guessing functionality if the user gets it wrong.
  guessed_number = 0
  while guessed_number != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guessed_number = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if the user gets it wrong.
    turns = checking(guessed_number, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guessed_number != answer:
      print("Guess again.")

  
game()
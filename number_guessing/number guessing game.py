import random
import art

HARD = 5
EASY = 10

def check_answer(compuer_choice, user_choice, turns):
	if user_choice > compuer_choice:
		print("Too High")
		return turns - 1
	elif user_choice < compuer_choice:
		print("Too Low")
		return turns - 1
	else:
		print("Congrats, you guessed the number right! ")
	

def difficulity():
	level = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
	if level == 'easy':
		return EASY
	elif level == 'hard':
		return HARD
	
	
def game():
	print(art.logo)
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	
	turns = difficulity()
	guess = 0
	answer = random.randint(1,100)
	
	while guess != answer:
		print(f"You have {turns} chances left.")
		guess = int(input("Make a guess: "))
		turns = check_answer(answer, guess, turns)
		if turns == 0:
			print(f"You lost.")
			return
		elif guess != answer:
			print("Try Again. ")


game()




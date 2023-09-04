import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
EASY_LEVEL_TURNS = 10
HIGH_LEVEL_TURNS = 5

def check_answer(guess,answer,turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess>answer:
        print("Too High")
        return turns-1
    elif guess<answer:
        print("Too low")
        return turns -1
    else:
        print(f"You've got the correct answer {answer}")

def set_difficulty():
    level = input("Choose difficulty level : Type 'easy' or 'hard': ")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HIGH_LEVEL_TURNS
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Pssst, the correct answer is {answer}") 
    turns = set_difficulty()
    guess = 0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Enter your guess:  "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess!=answer:
            print('guess again')
game()


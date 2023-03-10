'''
----------------------------------------
   File: RPS_Remade.py
Project: Remoke of Paper, Scissors, Rock
 Author: Vexnos
   Date: 2023-03-10
----------------------------------------
'''
#-------Libraries-------
from random import choice

#-------Globals-------
choices = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

#-------Functions-------
def user_choice():
    inputting = True
    while inputting:
        user = input("Pick between Rock, Paper, or Scissors: ").upper()
        if len(user) > 0:
            if user[0] in choices:
                return choices[user]
        print("Invalid choice, please try again")

def ai_choice():
    ai = choice(list(choices.values()))
    return ai

def faceoff(user, ai):
    print(f"You: {user}, AI: {ai}")

    # Tie
    if user == ai:
        print(f"Both players picked {user}! It's a tie!")

    # User picked Rock
    elif user == "Rock":
        # AI picked Scissors
        if ai == "Scissors":
            print(f"{user} crushes {ai}! You win!")
        # AI picked Paper
        else:
            print(f"{ai} covers {user}! You lose!")

    # User picked Paper
    elif user == "Paper":
        # AI picked Rock
        if ai == "Rock":
            print(f"{user} covers {ai}! You win!")
        # AI picked Scissors
        else:
            print(f"{ai} cuts {user}! You lose!")

    # User picked Scissors
    else:
        # AI picked Paper
        if ai == "Paper":
            print(f"{user} cuts {ai}! You win!")
        # Ai picked Rock
        else:
            print(f"{ai} crushes {user}! You lose!")

#-------Main Routine-------
if __name__ == "__main__": 
    playing = True
    while playing:
        user = user_choice()
        ai = ai_choice()
        faceoff(user, ai)

        play_again = input("\nWant to play again? (y/n): ")
        playing = play_again.lower().startswith("y")
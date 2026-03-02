import random
letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
attempts = 0
print("Welcome to Letter Guessing Game")
print("Enter a letter between A to Z")
while True:
    guess = input("Enter the letter: ").upper()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter (A-Z)")
        continue
    attempts += 1
    if guess > letter:
        print("Too High")
    elif guess < letter:
        print("Too Low")
    else:
        print("You Found The Correct Letter!")
        print("Total Attempts:", attempts);
        break

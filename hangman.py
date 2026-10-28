import random

WORDS = ["python", "coding", "laptop", "program", "hangman"]
word = random.choice(WORDS)
guessed, wrong = [], 0

while wrong < 6:
    shown = " ".join(c if c in guessed else "_" for c in word)
    print(f"\n{shown}   (wrong guesses: {wrong}/6)")
    if "_" not in shown:
        print("You won!")
        break
    guess = input("Guess a letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Enter one letter.")
    elif guess in guessed:
        print("Already guessed.")
    else:
        guessed.append(guess)
        if guess not in word:
            wrong += 1
else:
    print(f"You lost! The word was '{word}'.")

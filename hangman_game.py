import random
def hangman():
    words = ["apple", "tiger", "chair", "robot", "plant"]
    word = random.choice(words)
    guessed = []
    attempts = 6
    while attempts > 0:
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "
        print(display.strip())
        print("Attempts:", attempts)
        guess = input("Enter letter: ").lower()
        if guess in guessed:
            continue
        guessed.append(guess)
        if guess not in word:
            attempts -= 1
        if all(letter in guessed for letter in word):
            print("You won! Word:", word)
            return
    print("You lost! Word:", word)
hangman()

secretWord = "python"

print("Here is the hidden secret word: ", end="")
for letter in secretWord:
    print("_ ", end="")
print("\n")

print("You only have 2 wrong guesses before the full body is hanged. \n")
guessedString = []
hangman = ["head", "head and chest", "full body"] 
wrongGuess = []

while len(guessedString) != len(secretWord):
    guess = input("Guess a letter:")

    if guess in secretWord:
        guessedString.append(guess)

        for letter in secretWord:
            if letter == guess or letter in guessedString:
                print(f"{letter} ", end="")
            else:
                print("_ ", end="")
        print("\n")

    else:
        wrongGuess.append(guess)
        if len(wrongGuess) == 1:
            print(f"{hangman[0]}\n")
        elif len(wrongGuess) == 2:
            print(f"{hangman[1]}\n")
        elif len(wrongGuess) == 3:
            print(f"{hangman[2]}\n")
            print("game over, you lost")
            exit()

if len(guessedString) == len(secretWord):
    print("Congratulations, you won")

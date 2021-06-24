word = "Secret"


allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    done = True

    guess = input(f"Allowed Errors left {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break
    done = True

    for letter in word:
        if letter.lower() not in guesses:
            done = False
if done:
    print(f"You found the word! It was {word}!")
else:
    print(f"Game Over! The word was {word}!")
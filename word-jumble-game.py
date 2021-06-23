# The computer picks a random word from a group and
# then creates a jumbled version of it, where the letters
# are in random order. The player has to guess the original
# word to win the game.
import random

print("Welcome to the Word Jumble Game")

# Create a group of words
words = ("abolish", "zone", "humanity", "return",
         "charge", "motorist", "migration")

# Pick a random word
random_word = words[random.randrange(len(words))]


# Jumble the word

# Create an empty string for the jumbled word and an empty list of the indexes of the jumbled word
jumbled_indexes = []
jumbled_word = ""


# To ensure that the length of the indexes are equal to the length of the random word
while len(jumbled_indexes) != len(random_word):

    random_number = random.randrange(len(random_word))
    # Ensures that the index is not currently present in the list
    if jumbled_indexes.count(random_number) == 0:
        jumbled_indexes.append(random_number)
        jumbled_word += random_word[random_number]
    else:
        continue


# Prompt the user to guess the word
print(f"The jumbled word is: {jumbled_word}")

tries = 3
while tries > 0:
    user_guess = input("Make your guess:")
    if user_guess == random_word:
        print(f"You are correct. The word is {random_word}")
        break
    else:
        tries -= 1
        print(f"Wrong word. You have {tries} more guesses left")


if tries == 0:
    print(f"Bad luck, the word was {random_word}")

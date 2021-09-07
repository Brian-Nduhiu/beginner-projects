import random

words = ["constraint", "initiative", "different", "regard", "sunrise"]

randomWord = words[random.randint(0,len(words) - 1)]

# print(randomWord)

jumbledWord = ""

indexlist = []

for i in range(len(randomWord)):
    indexlist.append(i)

# print(indexlist)

randomlist = []

while len(randomlist) != len(indexlist):
    randnum = random.randint(0, len(indexlist)-1)
    if randnum not in randomlist:
        randomlist.append(randnum)
    
# print(randomlist)

for i in randomlist:
    jumbledWord += randomWord[i]

print(f"The Jumbled Word is {jumbledWord}")

guess = input("Guess the word: ")

if guess == randomWord:
    print(f"Correct the random word is {randomWord}")

else:
    print(f"Sorry, the random word is {randomWord}")




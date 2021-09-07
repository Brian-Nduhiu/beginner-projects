import random

words = ["constraint", "initiative", "different", "regard", "sunrise"]

randomWord = words[random.randint(0,len(words) - 1)]

# print(randomWord)

jumbledWord = ""

while len(jumbledWord) != len(randomWord):
    
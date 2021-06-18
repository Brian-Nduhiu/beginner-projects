#  This file contains some of the trial code I use to test various concepts in python


# Printing the word Game Over with the use of symbols
# print("""
#      ______
#     |
#     |
#     |
#     |
#     |_______|


#        _____       ___       ___  ___   _____
#       /  ___|     /   |     /   |/   | |  ___|
#       | |        / /| |    / /|   /| | | |__
#       | |  _    / ___ |   / / |__/ | | |  __|
#       | |_| |  / /  | |  / /       | | | |___
#       \_____/ /_/   |_| /_/        |_| |_____|
#       _____   _     _   _____   _____
#       /  _  \ | |   / / |  ___| |  _  \
#       | | | | | |  / /  | |__   | |_| |
#       | | | | | | / /   |  __|  |  _  /
#       | |_| | | |/ /    | |___  | | \ \
#       \_____/ |___/     |_____| |_|  \_\ """)

# Use of the 'end' parameter in print to specify what I want to be the last character in my print statement
# print("This is", end=" : ")
# print("Nairobi")

# Using double forward slashes to print out a forward slash
# print("\\")


# Using a forward slash to break a statement into two lines without causing an error
# if 1 > \
#         2:
#     print("one is greater than two")
# else:
#     print("two is greater than one")

# Printing the difference between the arithmetic operator / and //
# print(7/2)
# print(7//2)

# Use of Input and converting the string to uppercase letters
# name = input("Enter your name: ")
# print(f"Welcome {name.upper()}")

# Importing the random class and using randint and randrange to generate random numbers
# import random
# die1 = random.randint(1, 6)
# die2 = random.randrange(6)+1
# print(f"You have selected {die1} and {die2}")


# A login simulator that simulates a login page where the password is secret
# print(f"Welcome to the login simulator \n")
# user_key = input("Please enter your password: ")
# if user_key == 'secret':
#     print(f"access granted \n")
# else:
#     print(f"access denied \n")


# A program that tries to detect and show you your mood based on the random numbers it generates
# import random
# print("I sense your energy.  Your true emotions are coming across my screen.")
# print("You are...")
# mood = random.randint(1, 3)

# if mood == 1:
#     # happy
#     print("""
#     -----------
#     |         |
#     | O    O  |
#     |   <     |
#     |         |
#     | .     . |
#     |  `...`  |
#     ----------- """)

# elif mood == 2:
#     # neutral
#     print("""
#      ------------
#      |          |
#      |  O    O  |
#      |    <     |
#      |          |
#      |  ------  |
#      |          |
#      ------------""")

# elif mood == 3:
#     # sad
#     print("""
#     -----------
#     |          |
#     |  O    O  |
#     |    <     |
#     |          |
#     |   .'.    |
#     |  '   '   |
#      ----------- """)

# else:
#     print("Illegal mood value!  (You must be in a really bad mood).")

# print("...today.")

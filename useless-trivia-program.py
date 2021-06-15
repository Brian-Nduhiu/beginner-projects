# The program takes three pieces of personal information from the user: name, age, and weight.
# From these mundane items, the program is able to produce some amusing but trivial facts about
# the person, such as how much the person would weigh on the moon.
# Though this may seem like a simple program ( and it is ), you’ll find that the program is more
# interesting  when  you  run  it  because  you’ve  had  input.
# You’ll  care  more  about  the  results because they’re personally tailored to you.

# Useless Trivia#
#
# Gets personal information from the user and then
# prints true but useless information about him or her

name = input("Hello, what is your name? \n")
age = float(input("How old are you? \n"))
weight = float(input("How much do you weigh in kilograms?\n"))


print(
    f"If Johnson Sakaja were to email you, he would address you as {name.title()} \nbut if he was mad, he would address you as {name.upper()}\n")

name += " "
print(
    f"If a small child was trying to get your attention, he would say: \n \"{name.title()*5}\" ")

seconds = age * 365 * 24 * 60 * 60
print(f"\nYou’re over {seconds} seconds old.\n")

moon_weight = weight / 6
print(
    f"\nDid you know that on the moon you would weigh only {moon_weight} kilograms?\n")

sun_weight = weight * 27.1
print(f"\nOn the sun, you'd weigh {sun_weight} (but, ah... not for long).\n")

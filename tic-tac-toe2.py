import random

# display the game instructions
# determine who goes first
# create an empty tic-tac-toe board
# display the board
# while nobody’s won and it’s not a tie
#   if it’s the human’s turn
#       get the human’s move
#       update the board with the move
#   otherwise
#       calculate the computer’s move
#   update the board with the move
#   display the board
#   switch turns
# congratulate the winner or declare a tie

# def instructions():
#     """ 
#        | 1 | 2 | 3 |

#        | 4 | 5 | 6 |
       
#        | 7 | 8 | 9 |
        
#         """
#     print(" Welcome to TIC TAC TOE \n")
#     position = 1
#     for i in range(3):
#         print("|", end="")
#         for j in range(3):
#             print(f" {position} |", end="")
#             position += 1
#         print("\n")
      


# def gameplay(player1):
#     move = 0
#     played = []
#     if player1 == 1:
#         move = random.randint(1,9)
#         print(move)
#         position = 1
#         iteration = position

#         for i in range(3):
#             print("|", end="")
#             for j in range(3):
#                 if move == iteration:
#                     print(f" {position} |", end="")
#                     iteration += 1
#                 else:
#                     print("  |", end="")

#             print("\n")




# def selectplayer():
#     # results => 1= computer 2= user 3= draw 
#     player1 = random.randint(1,2)
#     if player1 == 1:
#         print("Computer will start the game")
#         results = gameplay(player1)
#     else:
#         print("You will start the game")
#         results = gameplay(player1)

#     return results

    
# def winner():
#     print()





# # main

# instructions()

# selectplayer()
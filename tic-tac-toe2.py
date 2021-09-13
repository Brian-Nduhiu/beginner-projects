import random


# display the game instructions*

# determine who goes first*

# create an empty tic-tac-toe board
# display the board*


# while nobody’s won and it’s not a tie
#   if it’s the human’s turn
#       get the human’s move

#       update the board with the move

#   otherwise
#       calculate the computer’s move

#       update the board with the move
#   
#   display the board

#   switch turns


# congratulate the winner or declare a tie


def instructions():
    
    name = input("What is your name?")

    print(
        f"""
        Welcome to TIC TAC TOE {name}

        Here is the board:

        _____________
        | 1 | 2 | 3 |
        -------------
        | 4 | 5 | 6 |
        -------------
        | 7 | 8 | 9 |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾

        """
    )

def emptyBoard():
    print(
        f"""
        _____________
        |   |   |   |
        -------------
        |   |   |   |
        -------------
        |   |   |   |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾
        """
    )

def gameplay():
    winner = None
    players = ["computer", "user"]
    currentPlayer = random.choice(players)
    moves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    

# Possible wins
# 1. 123
# 2. 456
# 3. 789
# 4. 147
# 5. 258
# 6. 369
# 7. 159
# 8. 357

    while winner == None:
        
        if currentPlayer == "computer":
            move = random.randint(1, 9)
            moves[move - 1] = "X"
            print(
                f"""
                _____________
                | {moves[0]} | {moves[1]} | {moves[2]} |
                -------------
                | {moves[3]} | {moves[4]} | {moves[5]} |
                -------------
                | {moves[6]} | {moves[7]} | {moves[8]} |
                ‾‾‾‾‾‾‾‾‾‾‾‾‾

                """
            )
        else:
            move = input("Enter your move")
            moves[move - 1] = "X"
            print(
                f"""
                _____________
                | {moves[0]} | {moves[1]} | {moves[2]} |
                -------------
                | {moves[3]} | {moves[4]} | {moves[5]} |
                -------------
                | {moves[6]} | {moves[7]} | {moves[8]} |
                ‾‾‾‾‾‾‾‾‾‾‾‾‾

                """
            )



    return winner

# main
instructions()


emptyBoard()
gameplay()



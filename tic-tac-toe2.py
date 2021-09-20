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

# Possible wins
# 1. 123*
# 2. 456*
# 3. 789*
# 4. 147*
# 5. 258*
# 6. 369*
# 7. 159*
# 8. 357

def win(moves):
    print()
    if (moves[0] == moves[1] == moves[2] == "X") or\
       (moves[3] == moves[4] == moves[5] == "X") or\
       (moves[6] == moves[7] == moves[8] == "X") or\
       (moves[0] == moves[3] == moves[6] == "X") or\
       (moves[1] == moves[4] == moves[7] == "X") or\
       (moves[2] == moves[5] == moves[8] == "X") or\
       (moves[0] == moves[4] == moves[8] == "X") or\
       (moves[2] == moves[4] == moves[6] == "X"):

        winner = "computer"


    elif  (moves[0] == moves[1] == moves[2] == "O") or\
          (moves[3] == moves[4] == moves[5] == "O") or\
          (moves[6] == moves[7] == moves[8] == "O") or\
          (moves[0] == moves[3] == moves[6] == "O") or\
          (moves[1] == moves[4] == moves[7] == "O") or\
          (moves[2] == moves[5] == moves[8] == "O") or\
          (moves[0] == moves[4] == moves[8] == "O") or\
          (moves[2] == moves[4] == moves[6] == "O"):

        winner = "user"


    elif " " not in moves:

        winner = "draw"

    else:

        winner = None


    return winner



def gameplay():
    winner = None
    players = ["computer", "user"]
    currentPlayer = random.choice(players)
    moves = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    played = []
    

# Possible wins
# 1. 123*
# 2. 456*
# 3. 789*
# 4. 147*
# 5. 258*
# 6. 369*
# 7. 159*
# 8. 357

    while winner == None:

        
        if currentPlayer == "computer":
            move = random.randint(1, 9)
            while move in played:
                move = random.randint(1, 9)
            played.append(move)
            moves[int(move) - 1] = "X"
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
            currentPlayer = "user"
            winner = win(moves)
        else:
            move = input("Enter your move")
            while move in played:
                move = input("Enter your move")
            played.append(int(move))
            moves[int(move) - 1] = "O"
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
            currentPlayer = "computer"
            winner = win(moves)



    return winner

# main
instructions()


emptyBoard()
winner = gameplay()
print(f"{winner} won the game")



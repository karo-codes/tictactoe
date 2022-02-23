# ------------------------- IMPORTS ------------------------------------------------- #
import numpy as np
import time
# ------------------------- GAME SETUP ------------------------------------------------- #
print("Welcome to Tic-Tac-Toe!")
# set up a board
board = np.array([["1", "2", "3"],
                  ["4", "5", "6"],
                  ["7", "8", "9"]])

print(board)

# setup for game loop
on = True
# check for a diagonal win
def check_diag(player):
    global on
    if board[0][0] == player and board[1][1] == player and board[2][2] == player \
            or board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(f"{player} wins!")
        on = False
    # else:
    #     print("n/a")


# check for a horizontal or vertical win
def check_straight(player):
    global on
    if board[0][0] == player and board[0][1] == player and board[0][2] == player \
            or board[1][0] == player and board[1][1] == player and board[1][2] == player \
            or board[2][0] == player and board[2][1] == player and board[2][2] == player \
            or board[0][0] == player and board[1][0] == player and board[2][0] == player \
            or board[0][1] == player and board[1][1] == player and board[2][1] == player \
            or board[0][2] == player and board[1][2] == player and board[2][2] == player:
        print(f"{player} wins!")
        on = False
    # else:
    #     print("n/a")


# ------------------------- GAME LOOP ------------------------------------------------- #
# set up turn
turn = 1
while on:
    # possible game over condition
    if turn == 10:
        print("Game over - it's a tie")
        break
    # finish turn setup + make players
    if turn % 2 == 0:
        current_player = "O"
    else:
        current_player = "X"
    # get player input
    b = str(input(f"Enter the # of the slot you want to mark (current player: {current_player})  "))
    # check if the slot is already taken
    if b not in board:
        print("Sorry, that's already taken - try again")
        continue
    # insert their input into the board
    board[board == b] = current_player
    # show the new board state
    print(board)
    # check for wins
    check_diag(current_player)
    check_straight(current_player)
    # swap players
    turn += 1

time.sleep(5)
print("Thanks for playing! Goodbye.")
time.sleep(3)

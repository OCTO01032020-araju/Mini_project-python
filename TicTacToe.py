board = ["--", "--", "--",
         "--", "--", "--",
         "--", "--", "--"]

game_going = True
current_player = input("Choose a player X OR O : ")

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def play_game():
    display_board()

    global game_going

    while game_going:
        handle_turn(current_player)
        check_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


def handle_turn(player):
    print("Welcome to game!!!!!")
    index_no = int(input("Enter a number between 0 and 8 according to position : "))
    board[index_no] = player
    display_board()

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
        print("Now it's turn of player O : ")

    elif current_player == "O":
        current_player = "X"
        print("Now it's turn of player X : ")


def check_game_over():
    check_win()
    check_tie()


def check_win():
    global winner

    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = doagonal_winner
    else:
        winner = None


def check_row():
    global game_going

    row_1 = board[0] == board[1] == board[2] != "--"
    row_2 = board[3] == board[4] == board[5] != "--"
    row_3 = board[6] == board[7] == board[8] != "--"

    if row_1 or row_2 or row_3:
        game_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_column():
    global game_going

    col_1 = board[0] == board[3] == board[6] != "--"
    col_2 = board[1] == board[4] == board[7] != "--"
    col_3 = board[2] == board[5] == board[8] != "--"

    if col_1 or col_2 or col_3:
        game_going = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None


def check_diagonal():
    global game_going

    dig_1 = board[0] == board[4] == board[8] != "--"
    dig_2 = board[2] == board[4] == board[6] != "--"

    if dig_1 or dig_2:
        game_going = False

    if dig_1:
        return board[0]
    elif dig_2:
        return board[2]
    else:
        return None


def check_tie():
    global game_going

    if "--" not in board:
        game_going = False
        return True
    else:
        return False


play_game()
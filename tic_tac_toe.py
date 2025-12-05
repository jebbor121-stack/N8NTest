
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_win(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("That cell is already taken. Try again.")
        else:
            print("Invalid row or column. Please enter numbers between 0 and 2.")

if __name__ == "__main__":
    play_game()

from board import create_board, display_board
from game_logic import check_winner, is_draw, make_move


def play_game():
    board = create_board()
    current_symbol = "X"

    while True:
        display_board(board)

        try:
            position = int(input(f"Player {current_symbol}, choose a position (1-9): "))
        except ValueError:
            print("Please enter a whole number from 1 to 9.")
            continue

        if not make_move(board, position, current_symbol):
            print("That position is not available. Choose an empty position from 1 to 9.")
            continue

        winner = check_winner(board)
        if winner is not None:
            display_board(board)
            print(f"Player {winner} wins!")
            return

        if is_draw(board):
            display_board(board)
            print("The game is a draw.")
            return

        if current_symbol == "X":
            current_symbol = "O"
        else:
            current_symbol = "X"


def main():
    print("Welcome to Tic Tac Toe!")

    while True:
        play_game()
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()


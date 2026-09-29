WINNING_COMBINATIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def make_move(board, position, symbol):
    """Place a symbol in an empty position numbered from 1 to 9."""
    if position < 1 or position > 9:
        return False

    cell_index = position - 1
    if board[cell_index] is not None:
        return False

    board[cell_index] = symbol
    return True


def check_winner(board):
    """Return the winning symbol, or None when nobody has won yet."""
    for combination in WINNING_COMBINATIONS:
        first, second, third = combination
        if board[first] is not None and board[first] == board[second] == board[third]:
            return board[first]

    return None


def is_draw(board):
    """Return True when every cell is full and there is no winner."""
    return check_winner(board) is None and all(cell is not None for cell in board)
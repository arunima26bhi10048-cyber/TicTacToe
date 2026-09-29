def create_board():
    """Create an empty board with nine cells."""
    return [None, None, None, None, None, None, None, None, None]


def display_board(board):
    """Print the board, showing position numbers in empty cells."""
    cells = []
    for position, value in enumerate(board, start=1):
        if value is None:
            cells.append(str(position))
        else:
            cells.append(value)

    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print()
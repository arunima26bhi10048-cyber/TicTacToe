# Tic Tac Toe in Python

## Project overview

This is a two-player Tic Tac Toe game for the terminal. Player X and Player O take turns choosing one of the nine numbered cells. The game checks for a row, column, or diagonal of three matching symbols, and also reports a draw when the board is full. Players can start another round without restarting the program.

The project uses only Python's standard features and is split into small modules so each part has one clear job.

## Project files

| File | Purpose |
| --- | --- |
| `tic tac toe.py` | Runs the game, reads player input, and changes turns. |
| `board.py` | Creates and displays the nine-cell board. |
| `game_logic.py` | Checks moves, winning combinations, and draws. |

The two Python modules are imported by the main program. Keep all three files in the same folder.

## Requirements

- Python 3.8 or newer
- No third-party packages


Enter a position from 1 to 9 when asked. The displayed board shows the number of each empty position. Enter `y` after a round to play again.

## How the program works

The board is a list with nine cells. An empty cell contains `None`; a played cell contains `X` or `O`. The player-facing positions are numbered 1 to 9, so `make_move` subtracts 1 to find the matching list index.

`game_logic.py` stores the eight winning combinations as groups of three list indexes. `check_winner` compares the values in each group. `make_move` rejects numbers outside 1 to 9 and cells that are already taken. `is_draw` checks that all cells are full and no winner was found.

`board.py` displays the symbols in played cells and the position number in empty cells. The main program calls these functions, asks for input, and changes the current symbol after a valid move.

## Concepts demonstrated

- Writing and importing custom Python modules
- Functions, lists, indexes, and loops
- `if` statements and Boolean conditions
- Reading and validating terminal input
- Returning values from functions

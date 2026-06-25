"""Tic-Tac-Toe: Human (X) vs Unbeatable AI (O)

Features:
- 3x3 board, positions 1-9
- Human uses 'X' and goes first
- AI uses 'O' and plays optimally via Minimax
- Displays board after each move
- Prevents invalid moves
- Announces win/lose/draw

Run: python "tic_tac_toe.py"
"""

from typing import List, Optional


def print_board(board: List[str]) -> None:
    """Prints the board. Empty cells show their position number (1-9)."""
    display = [board[i] if board[i] != ' ' else str(i + 1) for i in range(9)]
    print()
    for r in range(3):
        row = ' | '.join(display[r * 3:(r + 1) * 3])
        print(' ' + row)
        if r < 2:
            print('---+---+---')
    print()


def check_winner(board: List[str]) -> Optional[str]:
    """Returns 'X' or 'O' if there's a winner, or None otherwise."""
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None


def is_board_full(board: List[str]) -> bool:
    return all(cell != ' ' for cell in board)


def minimax(board: List[str], is_maximizing: bool) -> int:
    """Minimax algorithm returning a score for the current board.

    Scores: +1 if AI ('O') wins, -1 if human ('X') wins, 0 for draw.
    """
    winner = check_winner(board)
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ' '
                if score < best_score:
                    best_score = score
        return best_score


def ai_move(board: List[str]) -> None:
    """Chooses the best move for AI ('O') using Minimax and applies it."""
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    if move != -1:
        board[move] = 'O'


def human_move(board: List[str]) -> None:
    """Prompts the human for a move (1-9) and applies it after validation."""
    while True:
        try:
            choice = input('Enter your move (1-9): ').strip()
            pos = int(choice) - 1
            if pos < 0 or pos > 8:
                print('Invalid position. Choose 1-9.')
                continue
            if board[pos] != ' ':
                print('Cell already taken. Pick another.')
                continue
            board[pos] = 'X'
            break
        except ValueError:
            print('Please enter a number between 1 and 9.')


def play_game() -> None:
    """Main game loop: human (X) goes first, AI (O) responds optimally."""
    board = [' '] * 9
    current = 'X'  # human starts

    print('Welcome to Tic-Tac-Toe! You are X. AI is O.')
    while True:
        print_board(board)

        if current == 'X':
            human_move(board)
        else:
            print('AI is thinking...')
            ai_move(board)

        winner = check_winner(board)
        if winner or is_board_full(board):
            print_board(board)
            if winner == 'X':
                print('You win! Congratulations!')
            elif winner == 'O':
                print('AI wins. Better luck next time.')
            else:
                print("It's a draw!")
            break

        current = 'O' if current == 'X' else 'X'


if __name__ == '__main__':
    play_game()


# Sample gameplay (example):
#
# Welcome to Tic-Tac-Toe! You are X. AI is O.
# 1 | 2 | 3
# ---+---+---
# 4 | 5 | 6
# ---+---+---
# 7 | 8 | 9
#
# Enter your move (1-9): 5
#
# 1 | 2 | 3
# ---+---+---
# 4 | X | 6
# ---+---+---
# 7 | 8 | 9
#
# AI is thinking...
#
# 1 | 2 | 3
# ---+---+---
# 4 | X | O
# ---+---+---
# 7 | 8 | 9
#
# ...game continues until win/draw

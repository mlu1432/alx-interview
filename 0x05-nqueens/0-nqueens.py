#!/usr/bin/python3
"""
N Queens Problem Solver.

This module contains a solution to the N Queens problem using backtracking.
It prints all the possible solutions for placing N queens on an NxN chessbo0ard
where no two queens threaten each other.

The script takes a single command-line argument,
which is the size of the chessboard N.
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The current board configuration where board[i]
                      is the column of the queen in the i-th row.
        row (int): The row where we want to place the queen.
        col (int): The column where we want to place the queen.
        n (int): The size of the board (NxN).

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    # Check the column for conflicts
    for i in range(row):
        if board[i] == col:
            return False

    # Check the left diagonal for conflicts
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check the right diagonal for conflicts
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False

    return True


def solve_n_queens(n):
    """
    Solve the N Queens problem and print all possible solutions.

    This function uses a backtracking approach to find all the ways
    to place N queens on an NxN chessboard so that no two
    queens threaten each other. It prints each
    solution as a list of lists, where each inner list represents
    a [row, column] position of a queen.

    Args:
        n (int): The size of the board (NxN).
    """
    def backtrack(board, row):
        """
        Backtracking helper function to place queens row by row.

        Args:
            board (list): The current board configuration.
            row (int): The current row to place the queen in.
        """
        if row == n:
            # Print the board configuration a list of positions [row, column]
            solution = [[i, board[i]] for i in range(n)]
            print(solution)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                # Place the queen at board[row][col]
                board[row] = col
                # Recur to place the next queen
                backtrack(board, row + 1)
                # Backtrack: remove the queen and try the next column
                board[row] = -1

    board = [-1] * n  # Initialize board with -1 meaning no queen placed
    backtrack(board, 0)  # Start backtracking from the first row


if __name__ == "__main__":
    """
    Main entry point for the N Queens problem solver.

    This part of the script handles command-line arguments and validates them.
    It checks if the provided argument is an integer greater than or equal to 4
    and then solves the N Queens problem for the given size.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if the argument is a valid integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # N must be at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Call the function to solve N Queens
    solve_n_queens(N)

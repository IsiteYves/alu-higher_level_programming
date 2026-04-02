#!/usr/bin/python3
"""N-Queens puzzle solver."""
import sys


def solve_nqueens():
    """Solve N-queens based on sys.argv."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        """Check if position is safe."""
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row):
        """Recursive backtracking."""
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    solve_nqueens()

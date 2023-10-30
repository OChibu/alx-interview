#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        print_solution(board, N)
        return

    for i in range(N):
        if is_safe(board, row, i, N):
            board[row][i] = 1
            solve_n_queens_util(board, row + 1, N)
            board[row][i] = 0

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_n_queens_util(board, 0, N)

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solve_n_queens(N)

    except ValueError:
        print("N must be a number")
        sys.exit(1)

if __name__ == "__main__":
    mai

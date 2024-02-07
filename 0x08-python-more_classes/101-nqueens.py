#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.

* Usage: nqueens N
-If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the status 1

* where N must be an integer greater or equal to 4
-If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
-If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1

* The program should print every possible solution to the problem
-One solution per line
-Format: see example
-You don’t have to print the solutions in a specific order

* You are only allowed to import the sys module
"""


def isSafe(m_queen, nqueen):
    """Method to Check if placing a queen at m_queen[nqueen]
    would result in conflicts.
    Args:
        m_queen: array that has the queens positions
        nqueen: queen number
    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill
    """

    row, col = nqueen, m_queen[nqueen]

    for i in range(nqueen):
        prev_row, prev_col = i, m_queen[i]

        if col == prev_col or abs(row - prev_row) == abs(col - prev_col):
            return False

    return True


def print_result(m_queen, nqueen):
    """Method that prints the positions of queens on the chessboard.
    Args:
        m_queen: array that has the queens positions
        nqueen: queen number
    """

    print("[", end="")
    for i in range(nqueen):
        print(f"[{i}, {m_queen[i]}]", end="")
        if i != nqueen - 1:
            print(", ", end="")
    print("]")


def Queen(m_queen, nqueen):
    """ Recursive method that executes the Backtracking algorithm
    Args:
        m_queen: array that has the queens positions
        nqueen: queen number
    """

    if nqueen is len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1

    for col in range(len(m_queen)):
        m_queen[nqueen] = col

        if isSafe(m_queen, nqueen):
            Queen(m_queen, nqueen + 1)


def solveNQueen(size):
    """ method that invokes the Backtracking algorithm
    Args:
        size: size of the chessboard
    """

    m_queen = [-1 for i in range(size)]

    Queen(m_queen, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQueen(size)

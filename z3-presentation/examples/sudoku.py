#!/usr/bin/env python
from z3 import * 
from boards import easy, expert, pretty_print_board
def square(n):
    for c in range(3):
        for r in range(3): 
            yield (r+(n//3)*3,c+(n%3)*3)
def col(n): 
    for i in range(9): yield (i, n)

def generate_solver(board):
    s = Solver() 
    solve = [[Int(str(r)+","+str(c)) for r in range(9)] for c in range(9)]
    for i,row in enumerate(board):
        for j,box in enumerate(row):
            if isinstance(box, int):
                s.add(solve[i][j] == box)
            s.add(1 <= solve[i][j], solve[i][j] <= 9)
    for i in range(9):
        s.add(*[Distinct(*solve[i])])
        s.add(Distinct([solve[r][c] for r,c in square(i)]))
        s.add(Distinct([solve[r][c] for r,c in col(i)]))
    return s,solve

def solve(board):
    solver,solved = generate_solver(board)
    c,m = solver.check(), solver.model()
    pretty_print_board(m, solved)

solve(easy)

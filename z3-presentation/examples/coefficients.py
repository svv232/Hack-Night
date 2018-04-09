#!/usr/bin/env python
from z3 import *
"""
produces solutions for equations in the form 
ax^2 + bx + c to go through some set of points
"""
def coefficients(points): #Works on 2 dimensions
    s = Solver()
    a,b,c = map(Int, ("a","b","c"))
    for x,y in points:
        s.add(a*(x**2) + b*x + c == y)
    s.check()
    return s.model()

def main():
    points = [
	(1,2),(-1,6), (2,3)
    ]
    print(coefficients(points))

if __name__ == "__main__":
    main()

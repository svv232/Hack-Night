#!/usr/bin/env python
from z3 import *

x,y,z = map(Int, "xyz")
s = Solver()

s.add(2*x + z == 3)
s.add(x - y - z == 1)
s.add(3*x - y == 4)

s.check()

print(s.model())

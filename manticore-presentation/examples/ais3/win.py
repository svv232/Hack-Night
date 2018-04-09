#!/usr/bin/env python
from manticore import Manticore

m = Manticore('./ais3_crackme', ['a'*30])

buffer_addr = 0
num_bytes = 30

@m.hook(0x4005cd)
def hook(state):
    state.cpu.EDI = 0x2

@m.hook(0x4005f3)
def hook(state):
    global buffer_addr
    solution = state.new_symbolic_buffer(num_bytes)
    for i,v in enumerate('ais3{'):
        state.constrain(solution[i] == ord(v))
    buffer_addr=state.cpu.read_int(state.cpu.RAX)
    state.cpu.write_bytes(buffer_addr, solution)

@m.hook(0x40060e)
def hook(state):
    state.abandon()

@m.hook(0x400602) #winning path
def hook(state):
    res = ''.join(map(chr, state.solve_buffer(buffer_addr, num_bytes)))
    print(res)
    m.terminate()

m.run()

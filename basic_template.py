from manticore import Manticore

#Manticore Object
m = Manticore("process_name", argv)

#function addresses

main = address_of_main
function_checking_input = address_of_function_checking_input

#global variables

buffer_address = address_of_input_buffer_in_program #address of user input
#size of the user input that affect execution and constraint solving
buffer_size = integer_size 

#function addresses

failure_address = address_of_execution_node_you_do_not_want_to_visit
winning_address = address_of_execution_node_you do_want_to_visit

@m.hook(main)
def hook(state):
    global buffer_address
    buffer_address = state.cpu.REGISTER_WITH_BUFFER_ADDRESS
    symbolic_buffer = state.new_symbolic_buffer(buffer_size)
    state.cpu.write_bytes(symbolic_buffer)

@m.hook(failure_address)
def hook(state):
    state.abandon()

@m.hook(winning_address)
def hook(state): #effectively solved for state or correct program input
    res = ''.join(map(chr, state.solver_buffer(buffer_addr, num_bytes)))
    print(res)
    m.terminate()

m.run()

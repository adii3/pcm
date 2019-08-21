##Prototype-1
##Generating some patterns using cellular Automata

def nextState(state):
    transition_rule={"111":"0", "110":"0", "101":"0", "100":"1", "011":"1", "010":"1", "001":"1", "000":"0"}
    next_state_string=""
    for cellnumber in range(0,len(state)):
        middle_cell=state[cellnumber]
        if cellnumber is 0:
            left_cell=state[len(state)-1]
            right_cell=state[cellnumber+1]
        elif cellnumber is len(state)-1:
            left_cell=state[cellnumber-1]
            right_cell=state[0]
        else:
            left_cell=state[cellnumber-1]
            right_cell=state[cellnumber+1]
        transition_rule_pattern="{0}{1}{2}".format(left_cell, middle_cell, right_cell)
        next_state_string=next_state_string+transition_rule[transition_rule_pattern]
    print(next_state_string)
    return next_state_string

start_state=('0'*41)+'1'+('0'*41)
print(start_state)
next_state=nextState(start_state)

for i in range(0,100):
    next_state=nextState(next_state)

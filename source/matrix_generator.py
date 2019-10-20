##Prototype-1
##Generating patterns using cellular Automata
import pygame

transition_dict={
    "30":{"111":"0", "110":"0", "101":"0", "100":"1",
                     "011":"1", "010":"1", "001":"1", "000":"0"},
    "150":{"111":"1", "110":"0", "101":"0", "100":"1",
                     "011":"0", "010":"1", "001":"1", "000":"0"},
    "18":{"111":"0", "110":"0", "101":"0", "100":"1",
                     "011":"0", "010":"0", "001":"1", "000":"0"},
    "109":{"111":"0", "110":"1", "101":"1", "100":"0",
                     "011":"1", "010":"1", "001":"0", "000":"1"}
    }

def nextState(state, transition_rule):
    next_state_string=""
    for cellnumber in range(0,len(state)):
        middle_cell=state[cellnumber]
        if cellnumber == 0:
            left_cell=state[len(state)-1]
            right_cell=state[cellnumber+1]
        else:
            left_cell=state[cellnumber-1]
            if(cellnumber == len(state)-1):
                right_cell=state[0]
            else:
                right_cell=state[cellnumber+1]
        transition_rule_pattern="{0}{1}{2}".format(left_cell, middle_cell, right_cell)
        next_state_string=next_state_string+transition_rule[transition_rule_pattern]
    #print(next_state_string)
    return next_state_string

def guiRepr(rectLength, cells, iterations, transition_rule):
    pygame.init()
    
    DISPLAY=pygame.display.set_mode((1920,1080), pygame.RESIZABLE)

    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)
    generateAndChart(DISPLAY, WHITE, BLUE, rectLength, cells, iterations, transition_rule)
    
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

def generateAndChart(DISPLAY, WHITE, BLUE, c, cells, iterations, transition_rule):
    rectLen=c
    rectBreadth=c
    yPerNewState=0
    xPerNewCell=0-rectLen
    start_state=('0'*cells)+'1'+('0'*cells)
    #start_state=('0'*int(cells/2))+'1'+('0'*int(cells/2))+('1'*int(cells/4))+('0'*2)
    for j in start_state:
        xPerNewCell=xPerNewCell+c
        if not j == '0':
            pygame.draw.rect(DISPLAY,BLUE,(xPerNewCell,yPerNewState,rectLen,rectBreadth))
    xPerNewCell=0-rectLen  
    yPerNewState=yPerNewState+c
    next_state=nextState(start_state, transition_rule)
        
    for i in range(0,iterations):
        next_state=nextState(next_state, transition_rule)
        for j in next_state:
            xPerNewCell=xPerNewCell+c
            if not j == '0':
                pygame.draw.rect(DISPLAY,BLUE,(xPerNewCell,yPerNewState,rectLen,rectBreadth))
        xPerNewCell=0-rectLen  
        yPerNewState=yPerNewState+c
    print("Cardinality of set of States in the Cellular Automaton: "+ str(2**(2*cells+1)))
    print("Number of iterations: "+ str(iterations))

def generateMatrix(start_state, iterations, transition_rule):
    matrix=[]
    next_state=nextState(start_state, transition_rule)
    
    matrix.append(start_state)
    matrix.append(next_state)

    for i in range(0,iterations):
        next_state=nextState(next_state, transition_rule)
        matrix.append(next_state)
    return matrix

#main()
#guiRepr(rectlength, cells, iterations, dict)
#(10, 50, 250)
#(5, 100, 700)
#(2, 150, 1500)
#guiRepr(2, 12, 150, transition_dict["109"])
#print(generateMatrix("0000001000000", 50, transition_dict["109"]))

from matrix_generator import *
import random

#print(generateMatrix("0000001000000", 50, transition_dict["109"]))

def extractionWindow(xLimit, yLimit):
    window=['0'*xLimit for i in range(0,yLimit)]
    return window

def startPos(xLimit, xSizeMatrix):
    xPos=random.randint(0,xSizeMatrix-xLimit)
    print([xPos, xPos+xLimit])
    return [xPos, xPos+xLimit]

def matrixGenerator(matrix, xLimit, yLimit):
    xSizeMatrix=len(matrix[0])
    if(xSizeMatrix<xLimit):
        print("Window Size too much")
    else:
        window=extractionWindow(xLimit, yLimit)
        
        windowMatrix=[list(window[i]) for i in range(0, len(window))]
        musicMatrix=[list(matrix[i]) for i in range(0, len(matrix))]

        startingPos=startPos(xLimit,xSizeMatrix)
        k=0
        yRand=random.randint(0, len(matrix)-4)
        print([yRand, yRand+4])
        for i in range(yRand, yRand+4):
            l=0
            for j in range(startingPos[0],startingPos[1]):
                windowMatrix[k][l]=int(windowMatrix[k][l])+int(musicMatrix[i][j])
                l=l+1
            k=k+1
        print(windowMatrix)
        return windowMatrix

#finalMatrix=matrixGenerator(generateMatrix("000000000010000000000", 50, transition_dict["109"]), 12, 4)


        
    


    
    
    

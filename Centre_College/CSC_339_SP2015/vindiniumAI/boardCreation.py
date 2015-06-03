#A program to generate random boards for vindinium

import random

def generateQBoard(size, liklihoodOfBarrier, liklihoodOfMine):
    board = [] 
    spawnLocation = random.randint(0, size * size)
    tavernLocation = random.randint(0, size * size)
    while tavernLocation == spawnLocation:
        tavernLocation = random.randint(0, size * size)

    #initialLine = "+"
    #for n in range(size * 2):
        #initialLine += "-"
    #board.append(initialLine)
    
    for i in range(size):
        #boardString = "|"
        boardString = ""
        for j in range(size):
            if spawnLocation == 0:
                boardString += "@1"
            elif tavernLocation == 0:
                boardString += "[]"
            elif random.random() < liklihoodOfBarrier:
                boardString += "##"
            elif random.random() < liklihoodOfMine:
                boardString += "$-"
            else:
                boardString += "  "

            spawnLocation -= 1
            tavernLocation -=1
        board.append(boardString)
        
    return board

def generateFBoard(size, liklihoodOfBarrier, liklihoodOfMine):
    fBoard = []
    qBoard = generateQBoard(size / 2, liklihoodOfBarrier, liklihoodOfMine)
    for row in qBoard:
        revRow = row[::-1]
        revRow = revRow.replace( "1@", "@4")
        revRow = revRow.replace( "][", "[]")
        revRow = revRow.replace( "-$", "$-")
        fBoard.append(row + revRow)

    bottomHalf = []
    for row in fBoard:
        row = row.replace( "1", "2")
        row = row.replace( "4", "3")
        bottomHalf.append(row)
    fBoard = fBoard + bottomHalf[::-1]

    return fBoard
    

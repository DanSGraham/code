#Chess game
#By Daniel Graham

from graphics import *

#Player 1 is white and goes first, player 2 is black and goes second.
## TO DO Get piece movement checking completed. Start with allowed movement directions. Move in one spuare movements.
## Add pawn promotion, castling, en passant, and check rules. ALso a game over condition.
##THE check function doesn't work.

class gameMediator:
    
    def addBoard(self, boardToAdd):
        self.board = boardToAdd

    def addPlayer1(self, player1ToAdd):
        self.player1 = player1ToAdd

    def addPlayer2(self, player2ToAdd):
        self.player2 = player2ToAdd

    def nextState(self, piece, position):
        ##This will check the next state of the game before the move takes place to see if the king is in check.
        print "Hello"

    def withinBoard(self, position):
        return (position[0] < 8 and position[0] > -1 and position[1] < 8 and position[1] > -1)

    def checkCheckMate(self, player):
        if player.getKing().isInCheck():
            for piece in player.getPieces():
                testStart = piece.getPosition()
                piecePossibleMoves = self.getPossibleMoves(piece)
                for piecePossibleMove in piecePossibleMoves:
                    piece.move(piecePossibleMove)
                    if not (self.checkKingCheck(piece)):
                        return False
            return True

    def takePiece(self, position):
        #Takes the piece at the position moved and replaces it with piece
        spaceToEdit = self.board.getSpaceAt(position)
        if spaceToEdit.getPiece() != None:
            pieceToRemove = spaceToEdit.getPiece()
            pieceToRemove.removeFromPlay()
            spaceToEdit.removePiece()

    def checkKingCheck(self, piece):
        #This methods determines if any potential moves will put your king into check.
        if piece.getColor() == "White":
            for testPiece in self.player2.getPieces():
                allSpaces = self.getPossibleMoves(testPiece)
                for testSpaces in allSpaces:
                    if testSpace == self.player1.getKing().getPosition():
                        self.player1.getKing().check()
                        return True
            self.player1.getKing().uncheck()
            return False
    
        if piece.getColor() == "Black":
            for testPiece in self.player1.getPieces():
                allSpaces = self.getPossibleMoves(testPiece)
                for testSpaces in allSpaces:
                    if testSpace == self.player2.getKing().getPosition():
                        self.player2.getKing().check()
                        return True
            self.player2.getKing().uncheck()
            return False

        
    def getPossibleMoves(self, piece):
        possibleMoves = []
        if piece.getType() == "Pawn":
            ## If moves off the board then swap for new piece.
            #Only works for white because they are moving forward...Need to allow it to check for other player.
            #For all other pieces they can go forwards or backwards so the direction doesn't matter, but for the pawn it can only go forward.
            #Pawn must change what it does depending on which player is using it.
            if piece.getColor() == "White":
                forwardOne = (piece.getPosition()[0] + 1, piece.getPosition()[1])
            else:
                forwardOne = (piece.getPosition()[0] - 1, piece.getPosition()[1])
            if(self.withinBoard(forwardOne)):
                if piece.getColor() == "White":
                    takeRight = (piece.getPosition()[0] + 1, piece.getPosition()[1] + 1)
                    takeLeft = (piece.getPosition()[0] + 1, piece.getPosition()[1] - 1)
                else:
                    takeRight = (piece.getPosition()[0] - 1, piece.getPosition()[1] + 1)
                    takeLeft = (piece.getPosition()[0] - 1, piece.getPosition()[1] - 1)
                    
                if self.board.getSpaceAt(forwardOne).getPiece() == None:
                    possibleMoves.append(forwardOne)
                    if piece.isFirstMove():
                        if piece.getColor() == "White":
                            forwardTwo = (piece.getPosition()[0] + 2, piece.getPosition()[1])
                        else:
                            forwardTwo = (piece.getPosition()[0] - 2, piece.getPosition()[1])
                            
                        if self.board.getSpaceAt(forwardTwo).getPiece() == None:
                            possibleMoves.append(forwardTwo)
                if self.isClear(piece, takeLeft) and self.withinBoard(takeLeft):
                    if self.board.getSpaceAt(takeLeft).getPiece() != None:
                        possibleMoves.append(takeLeft)
                if self.isClear(piece, takeRight) and self.withinBoard(takeRight):
                     if self.board.getSpaceAt(takeRight).getPiece() != None:
                         possibleMoves.append(takeRight)
                         
        if piece.getType() == "Rook":
            for i in range(1,8):
                forwardMove = ((piece.getPosition()[0] + i), piece.getPosition()[1])
                if self.withinBoard(forwardMove) and self.isClear(piece, forwardMove):
                    possibleMoves.append(forwardMove)
                    if self.board.getSpaceAt(forwardMove).getPiece() != None:
                        break
                else:
                    break

            for j in range(1,8):
                rightMove = (piece.getPosition()[0], piece.getPosition()[1] + j)
                if self.withinBoard(rightMove) and self.isClear(piece, rightMove):
                    possibleMoves.append(rightMove)
                    if self.board.getSpaceAt(rightMove).getPiece() != None:
                        break
                else:
                    break

            for k in range(1,8):
                backwardMove = (piece.getPosition()[0] - k, piece.getPosition()[1])
                if self.withinBoard(backwardMove) and self.isClear(piece, backwardMove):
                    possibleMoves.append(backwardMove)
                    if self.board.getSpaceAt(backwardMove).getPiece() != None:
                        break
                else:
                    break

            for m in range(1,8):
                leftMove = (piece.getPosition()[0], piece.getPosition()[1] - m)
                if self.withinBoard(leftMove) and self.isClear(piece, leftMove):
                    possibleMoves.append(leftMove)
                    if self.board.getSpaceAt(leftMove).getPiece() != None:
                        break
                else:
                    break
                
        if piece.getType() == "Knight":

            rookMoves = []
            longLRightForward = (piece.getPosition()[0] + 2, piece.getPosition()[1] + 1)
            longLLeftForward = (piece.getPosition()[0] + 2, piece.getPosition()[1] - 1)
            longLRightBackward = (piece.getPosition()[0] - 2, piece.getPosition()[1] + 1)
            longLLeftBackward = (piece.getPosition()[0] - 2, piece.getPosition()[1] - 1)
            shortLRightForward = (piece.getPosition()[0] + 1, piece.getPosition()[1] + 2)
            shortLLeftForward = (piece.getPosition()[0] + 1, piece.getPosition()[1] - 2)
            shortLRightBackward = (piece.getPosition()[0] - 1, piece.getPosition()[1] + 2)
            shortLLeftBackward = (piece.getPosition()[0] - 1, piece.getPosition()[1] - 2)
            rookMoves.append(longLRightForward)
            rookMoves.append(longLLeftForward)
            rookMoves.append(longLRightBackward)
            rookMoves.append(longLLeftBackward)
            rookMoves.append(shortLRightForward)
            rookMoves.append(shortLLeftForward)
            rookMoves.append(shortLRightBackward)
            rookMoves.append(shortLLeftBackward)
            
            for possibleRookMove in rookMoves:
                if self.withinBoard(possibleRookMove) and self.isClear(piece, possibleRookMove):
                    possibleMoves.append(possibleRookMove)

    
            
            
                
        if piece.getType() == "Bishop":
            for i in range(1,8):
                forwardRightMove = (piece.getPosition()[0] + i, piece.getPosition()[1] + i)
                if self.withinBoard(forwardRightMove) and self.isClear(piece, forwardRightMove):
                    possibleMoves.append(forwardRightMove)
                    if self.board.getSpaceAt(forwardRightMove).getPiece() != None:
                        break
                else:
                    break

            for j in range(1,8):
                backwardRightMove = (piece.getPosition()[0] - j, piece.getPosition()[1] + j)
                if self.withinBoard(backwardRightMove) and self.isClear(piece, backwardRightMove):
                    possibleMoves.append(backwardRightMove)
                    if self.board.getSpaceAt(backwardRightMove).getPiece() != None:
                        break
                else:
                    break

            for k in range(1,8):
                backwardLeftMove = (piece.getPosition()[0] - k, piece.getPosition()[1] - k)
                if self.withinBoard(backwardLeftMove) and self.isClear(piece, backwardLeftMove):
                    possibleMoves.append(backwardLeftMove)
                    if self.board.getSpaceAt(backwardLeftMove).getPiece() != None:
                        break
                else:
                    break

            for m in range(1,8):
                forwardLeftMove = (piece.getPosition()[0] + m, piece.getPosition()[1] - m)
                if self.withinBoard(forwardLeftMove) and self.isClear(piece, forwardLeftMove):
                    possibleMoves.append(forwardLeftMove)
                    if self.board.getSpaceAt(forwardLeftMove).getPiece() != None:
                        break
                else:
                    break
                
        if piece.getType() == "Queen":
            for i in range(1,8):
                forwardMove = (piece.getPosition()[0] + i, piece.getPosition()[1])
                if self.withinBoard(forwardMove) and self.isClear(piece, forwardMove):
                    possibleMoves.append(forwardMove)
                    if self.board.getSpaceAt(forwardMove).getPiece() != None:
                        break
                else:
                    break

            for j in range(1,8):
                rightMove = (piece.getPosition()[0], piece.getPosition()[1] + j)
                if self.withinBoard(rightMove) and self.isClear(piece, rightMove):
                    possibleMoves.append(rightMove)
                    if self.board.getSpaceAt(rightMove).getPiece() != None:
                        break
                else:
                    break

            for k in range(1,8):
                backwardMove = (piece.getPosition()[0] - k, piece.getPosition()[1])
                if self.withinBoard(backwardMove) and self.isClear(piece, backwardMove):
                    possibleMoves.append(backwardMove)
                    if self.board.getSpaceAt(backwardMove).getPiece() != None:
                        break
                else:
                    break

            for m in range(1,8):
                leftMove = (piece.getPosition()[0], piece.getPosition()[1] - m)
                if self.withinBoard(leftMove) and self.isClear(piece, leftMove):
                    possibleMoves.append(leftMove)
                    if self.board.getSpaceAt(leftMove).getPiece() != None:
                        break
                else:
                    break
            for n in range(1,8):
                forwardRightMove = (piece.getPosition()[0] + n, piece.getPosition()[1] + n)
                if self.withinBoard(forwardRightMove) and self.isClear(piece, forwardRightMove):
                    possibleMoves.append(forwardRightMove)
                    if self.board.getSpaceAt(forwardRightMove).getPiece() != None:
                        break
                else:
                    break

            for p in range(1,8):
                backwardRightMove = (piece.getPosition()[0] - p, piece.getPosition()[1] + p)
                if self.withinBoard(backwardRightMove) and self.isClear(piece, backwardRightMove):
                    possibleMoves.append(backwardRightMove)
                    if self.board.getSpaceAt(backwardRightMove).getPiece() != None:
                        break
                else:
                    break

            for q in range(1,8):
                backwardLeftMove = (piece.getPosition()[0] - q, piece.getPosition()[1] - q)
                if self.withinBoard(backwardLeftMove) and self.isClear(piece, backwardLeftMove):
                    possibleMoves.append(backwardLeftMove)
                    if self.board.getSpaceAt(backwardLeftMove).getPiece() != None:
                        break
                else:
                    break

            for r in range(1,8):
                forwardLeftMove = (piece.getPosition()[0] + r, piece.getPosition()[1] - r)
                if self.withinBoard(forwardLeftMove) and self.isClear(piece, forwardLeftMove):
                    possibleMoves.append(forwardLeftMove)
                    if self.board.getSpaceAt(forwardLeftMove).getPiece() != None:
                        break
                else:
                    break

        if piece.getType() == "King":
            forwardMove = (piece.getPosition()[0] + 1, piece.getPosition()[1])
            if self.withinBoard(forwardMove) and self.isClear(piece, forwardMove):
                possibleMoves.append(forwardMove)
                    
            rightMove = (piece.getPosition()[0], piece.getPosition()[1] + 1)
            if self.withinBoard(rightMove) and self.isClear(piece, rightMove):
                possibleMoves.append(rightMove)

            backwardMove = (piece.getPosition()[0] - 1, piece.getPosition()[1])
            if self.withinBoard(backwardMove) and self.isClear(piece, backwardMove):
                possibleMoves.append(backwardMove)

            leftMove = (piece.getPosition()[0], piece.getPosition()[1] - 1)
            if self.withinBoard(leftMove) and self.isClear(piece, leftMove):
                possibleMoves.append(leftMove)
            
            forwardRightMove = (piece.getPosition()[0] + 1, piece.getPosition()[1] + 1)
            if self.withinBoard(forwardRightMove) and self.isClear(piece, forwardRightMove):
                possibleMoves.append(forwardRightMove)
                    
            backwardRightMove = (piece.getPosition()[0] - 1, piece.getPosition()[1] + 1)
            if self.withinBoard(backwardRightMove) and self.isClear(piece, backwardRightMove):
                possibleMoves.append(backwardRightMove)
                   
            backwardLeftMove = (piece.getPosition()[0] - 1, piece.getPosition()[1] - 1)
            if self.withinBoard(backwardLeftMove) and self.isClear(piece, backwardLeftMove):
                possibleMoves.append(backwardLeftMove)
                    
            forwardLeftMove = (piece.getPosition()[0] + 1, piece.getPosition()[1] - 1)
            if self.withinBoard(forwardLeftMove) and self.isClear(piece, forwardLeftMove):
                possibleMoves.append(forwardLeftMove)
                                
        print possibleMoves            
        return possibleMoves

    def isClear(self, piece, position):
        potentialPosition = self.board.getSpaceAt(position)
        if potentialPosition.getPiece() != None:
            if potentialPosition.getPiece().getColor() == piece.getColor():
                return False
            else:
                return True
        else:
            return True

    def movePiece(self, piece, position):
        potentialMoves = self.getPossibleMoves(piece)
        if position in potentialMoves:
            self.takePiece(position)
            self.board.getSpaceAt(piece.getPosition()).removePiece()
            piece.move(position)
            self.board.getSpaceAt(position).addPiece(piece)

class boardSpace:
    
    def __init__(self, xPos, yPos):
        self.piece = None
        self.xPos = xPos
        self.yPos = yPos

    def getPiece(self):
        return self.piece

    def addPiece(self, piece):
        self.piece = piece

    def removePiece(self):
        self.piece = None

    def __str__(self):
        if self.piece == None:
            return "X"
        else:
            return str(self.piece)
        
class board:

    def __init__(self, mediator):
        self.mediator = mediator
        self.boardGrid = []
        for i in range(8):
            self.boardGrid.append([])
            for j in range(8):
                self.boardGrid[i].append(boardSpace(i, j))

    def addPiece(self, piece):
        self.boardGrid[piece.getPosition()[0]][piece.getPosition()[1]].addPiece(piece)

    def removePiece(self, piece):
        self.boardGrid[piece.getPosition()[0]][piece.getPosition()[1]].removePiece(piece)

    def getSpaceAt(self, coordinates):
        return self.boardGrid[coordinates[0]][coordinates[1]]
    
    def __str__(self):
        stringToBuild = ""
        for i in range(8):
            for j in range(8):
                stringToBuild += str(self.boardGrid[i][j])
            stringToBuild += "\n"
        return stringToBuild


class Piece:

    def __init__(self, position, typeOfPiece, owner):
        self.owner = owner
        self.type = typeOfPiece
        self.position = position

    def assignColor(self, color):
        self.color = color

    def getOwner(self):
        return self.owner

    def getColor(self):
        return self.color

    def move(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def removeFromPlay(self):
        removePiece = None
        for piece in self.owner.getPieces():
            if piece == self:
                removePiece = piece
                print "WORKS"
        self.owner.getPieces().remove(removePiece)

    def getType(self):
        return self.type

    def __str__(self):
        return self.type[0]

class Pawn(Piece):

    def __init__(self, position, owner):
        self.owner = owner
        self.position = position
        self.type = "Pawn"
        self.firstMove = True

    def move(self, position):
        self.position = position
        self.firstMove = False

    def isFirstMove(self):
        return self.firstMove

    def __str__(self):
        return "P"
    
class King(Piece):

    def __init__(self, position, owner):
        self.owner = owner
        self.position = position
        self.type = "King"
        self.inCheck = False

    def isInCheck(self):
        return self.inCheck

    def check(self):
        self.inCheck = True

    def unCheck(self):
        self.inCheck = False

    def __str__(self):
        return "G"

class Player:

    def __init__(self, color, mediator):
        self.mediator = mediator
        self.pieces = []
        self.color = color
        if color == "White":
            rook1 = Piece((0,0), "Rook", self)
            rook2 = Piece((0,7), "Rook", self)
            knight1 = Piece((0,1), "Knight", self)
            knight2 = Piece((0,6), "Knight", self)
            bishop1 = Piece((0,2), "Bishop", self )
            bishop2 = Piece((0,5), "Bishop", self)
            queen = Piece((0,3), "Queen", self)
            self.king = King((0,4), self)
            for i in range(8):
                pawn = Pawn((1,i), self)
                self.pieces.append(pawn)
                
        if color == "Black":
            rook1 = Piece((7,0), "Rook", self)
            rook2 = Piece((7,7), "Rook", self)
            knight1 = Piece((7,1), "Knight", self)
            knight2 = Piece((7,6), "Knight", self)
            bishop1 = Piece((7,2), "Bishop", self)
            bishop2 = Piece((7,5), "Bishop", self)
            queen = Piece((7,3), "Queen", self)
            self.king = King((7,4), self)
            for i in range(8):
                pawn = Pawn((6,i), self)
                self.pieces.append(pawn)

        self.pieces.append(rook1)
        self.pieces.append(rook2)
        self.pieces.append(knight1)
        self.pieces.append(knight2)
        self.pieces.append(bishop1)
        self.pieces.append(bishop2)
        self.pieces.append(queen)
        self.pieces.append(self.king)
        for piece in self.pieces:
            piece.assignColor(self.color)
        
    def getPieces(self):
        return self.pieces

    def getColor(self):
        return self.color

    def getKing(self):
        return self.king

    def movePiece(self, pieceToMove, startingPosition, endingPosition):
        for piece in self.pieces:
            if piece.getType() == pieceToMove and piece.getPosition() == startingPosition:
                self.mediator.movePiece(piece, endingPosition)

class Game:
    def __init__(self):
        self.mediator = gameMediator()
        self.board = board(self.mediator)
        self.player1 = Player("White", self.mediator)
        self.player2 = Player("Black", self.mediator)
        playerList = []
        for piece in self.player1.getPieces():
            self.board.addPiece(piece)
        for piece in self.player2.getPieces():
            self.board.addPiece(piece)
        print self.board
        self.mediator.addBoard(self.board)
        self.mediator.addPlayer1(self.player1)
        self.mediator.addPlayer2(self.player2)
        playerList.append(self.player1)
        playerList.append(self.player2)
        currPlayer = 0
        while not self.mediator.checkCheckMate(playerList[currPlayer%2]):
            pieceToMove, startMove, endMove = input(playerList[currPlayer%2].getColor() + ", Enter a Move ('NAME_OF_PIECE', (startingCoord), (endingCoord))")
            playerList[currPlayer%2].movePiece(pieceToMove, startMove, endMove)
            print self.board
            currPlayer += 1
        currPlayer += 1
        print playerList[currPlayer%2].getColor() + " is the winner!"

def main():
    test = Game()


from tkinter import *
import tkinter
import time
import numpy
import unittest


class GameView:
    def __init__(self,model,controller):
        self.fileList = ["Pawn_W.png","Pawn_B.png","Knight_W.png","Knight_B.png","Bishop_W.png","Bishop_B.png","Rook_W.png","Rook_B.png","Queen_W.png","Queen_B.png","King_W.png","King_B.png","tile_khaki.png","tile_pink.png","SideMod.png","backbutt.png","playbutt.png","editbutt.png","exitbutt.png"]
        self.view = Tk()
        self.Tsize = 50
        self.winW = self.Tsize*8
        self.winH = self.Tsize*8
        self.modW = self.Tsize*2
        self.model = model
        self.controller = controller
        self.win = Canvas(self.view, width = self.winW+100, height = self.winH)
        self.win.pack()
        self.imageList = [PhotoImage(file="C:\\Users\\Ethan\\Source\Repos\\Chess-Python\\Graphics\\" + i) for i in self.fileList]
        
        self.boardImage = PhotoImage(file="C:\\Users\\Ethan\\Source\Repos\\Chess-Python\\Graphics\\" + "ChessBoard.png")
        self.promotePiece = 0
    def placePiece(self,piece, x, y):
        if (piece>0):
            self.win.create_image(x-25,y-25,image = self.imageList[piece-1])
    def buttonOutline(self,buttonSelected):
        self.win.create_rectangle(9*self.Tsize-50,(buttonSelected-1)*50,9*self.Tsize+50,buttonSelected*50)
        self.win.update()
        time.sleep(.2)
    
    def updateSideBar(self):
        self.placePiece(15,9*self.Tsize+25,4*self.Tsize+25)
        if (self.controller.gameMode == 'menu'):
            self.placePiece(17,9*self.Tsize+25,self.Tsize)
            self.placePiece(18,9*self.Tsize+25,2*self.Tsize)
            self.placePiece(19,9*self.Tsize+25,8*self.Tsize)
            #self.win.create_rectangle(9*self.Tsize-50,50,9*self.Tsize+50,100)

        if (self.controller.gameMode == 'play'):
            self.placePiece(16,9*self.Tsize+25,8*self.Tsize)
        if (self.controller.gameMode == 'edit'):
            self.placePiece(17,9*self.Tsize+25,self.Tsize)
            self.placePiece(16,9*self.Tsize+25,8*self.Tsize)
            for x in range(2):
                for y in range(6):
                    #print(self.controller.selectedX, "must equal ", x+8)
                    #print(self.controller.selectedY, "must equal ", y+1)
                    if(x+8 == self.controller.selectedX and y+1 == self.controller.selectedY):
                        print("bruh2")
                        self.placePiece(13,(x+9)*self.Tsize,(y+2)*self.Tsize)
                    self.placePiece(self.controller.editPieces[x][y],(x+9)*self.Tsize,(y+2)*self.Tsize)
                    
            

            
        
    
    def updateScreen(self): 
        self.win.delete('all')
        self.win.create_image(self.winW/2,self.winH/2, image = self.boardImage)
        self.placeSpecialTiles()

        self.updateSideBar()

        if (self.controller.whitesMove):
            
            for x in range(8):
                for y in range(8):
                    self.placePiece(self.model.getPieceAt(x,y),(x+1)*self.Tsize,(y+1)*self.Tsize)
            self.win.update()
        else:
            
            for x in range(8):
                for y in range(8):
                    self.placePiece(self.model.getPieceAt(7-x,7-y),((x+1))*self.Tsize,((y+1))*self.Tsize)
            self.win.update()
        
        
    def placeSpecialTiles(self):
        blackKing = self.model.findPiece(12)
        whiteKing = self.model.findPiece(11)
        #print(self.model.whiteKingChecks(), " ", len(self.model.whiteKingChecks()))
        if (self.controller.selected):
            self.placePiece(13,(self.controller.selectedX+1)*self.Tsize,(self.controller.selectedY+1)*self.Tsize)
        if(len(self.model.blackKingChecks()) > 0):
            print("oh")
            if(self.controller.whitesMove):
                self.placePiece(14,(blackKing[0]+1)*self.Tsize,(blackKing[1]+1)*self.Tsize)
            else:
                self.placePiece(14,(7-blackKing[0]+1)*self.Tsize,(7-blackKing[1]+1)*self.Tsize)
        if(len(self.model.whiteKingChecks()) > 0):
            print(whiteKing[0], " ", whiteKing[1])
            if(self.controller.whitesMove):
                self.placePiece(14,(whiteKing[0]+1)*self.Tsize,(whiteKing[1]+1)*self.Tsize)
            else:
                self.placePiece(14,(7-whiteKing[0]+1)*self.Tsize,(7-whiteKing[1]+1)*self.Tsize)
    def promotePrompt(self):
        button = tkinter.Tk()

        def Queen():
            if (self.controller.whitesMove):
                self.promotePiece = 9
            else:
                self.promotePiece = 10
            button.quit()
            button.destroy()
        def Rook():
            if (self.controller.whitesMove):
                self.promotePiece = 7
            else:
                self.promotePiece = 8
            button.quit()
            button.destroy()
        def Bishop():
            if (self.controller.whitesMove):
                self.promotePiece = 5
            else:
                self.promotePiece = 6
            button.quit()
            button.destroy()
        def Knight():
            if (self.controller.whitesMove):
                self.promotePiece = 3
            else:
                self.promotePiece = 4
            button.quit()
            button.destroy()
        
        queen = tkinter.Button(button, text ="Queen", command = Queen)
        rook = tkinter.Button(button, text ="Rook", command = Rook)
        bishop = tkinter.Button(button, text ="Bishop", command = Bishop)
        knight = tkinter.Button(button, text ="Knight", command = Knight)
        queen.pack()
        rook.pack()
        bishop.pack()
        knight.pack()
        button.mainloop()
        return self.promotePiece
class GameModel:
    def __init__(self):
        self.initBoardData = numpy.array([[8,4,6,10,12,6,4,8],[2,2,2,2,2,2,2,2],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[7,3,5,9,11,5,3,7]])
        self.emptyBoard = numpy.array([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
        self.boardData = self.emptyBoard
        self.enPass = None
        self.checked = False
        self.needsPromotionAt = None 

    def setUpBoard(self,board):
        self.boardData = board
    def doPromotionAt(self,whitesMove,piece):
        if (whitesMove):
            self.placePieceAt(piece,self.needsPromotionAt,0)
        else:
            self.placePieceAt(piece,self.needsPromotionAt,7)
        self.needsPromotionAt = None

    def getPieceAt(self,x,y):
        if (x < 0 or x > 7 or y < 0 or y > 7):
            return 0
        return self.boardData[y,x]
    def removePieceAt(self,x,y):
        self.boardData[y,x] = 0
    def placePieceAt(self,piece, x, y):
        self.boardData[y,x] = piece
    def blockRule(self,x,y,X,Y):
        xStep = 0
        yStep = 0
        if (X-x != 0):
            xStep = int((X-x)/abs(X-x))
            pathLength = abs(X-x)
        if (Y-y != 0):
            yStep = int((Y-y)/abs(Y-y))
            pathLength = abs(Y-y)

        for i in range(1,pathLength):
            xShift = x+i*xStep
            yShift = y+i*yStep

            if (xShift < 0 or xShift > 7 or yShift < 0 or yShift > 7):
                return [0,None,None]
            thispiece = self.getPieceAt(xShift,yShift)
            if (thispiece != 0):
                return [thispiece,xShift,yShift]
        return [0,None,None]
    def findPiece(self,piece):
        for i in range(8):
            for j in range(8):
                if self.boardData[i,j] == piece:
                    return [j,i]
        return [0,0]

    def blackKingChecks(self):
        kingPos = self.findPiece(12)
        print(kingPos)
        #print("blackKing: ",self.squareAttackers(4,0,True))
        return self.squareAttackers(4,0,True)
    def whiteKingChecks(self):
        kingPos = self.findPiece(11)
        print(kingPos)
        #print("whiteKing: ",self.squareAttackers(4,7,False))
        return self.squareAttackers(4,7,False)


    def squareAttackers(self,X,Y,attackerIsWhite):
        #kingCoords = findPiece(12)
        #X = kingCoords[0]
        #Y = kingCoords[1]
        piece = self.getPieceAt(X,Y)

        attackers = []

        straightChecks = [self.blockRule(X,Y,X,8),self.blockRule(X,Y,X,-1),self.blockRule(X,Y,8,Y),self.blockRule(X,Y,-1,Y)]
        diagonalChecks = [self.blockRule(X,Y,X+8,Y+8),self.blockRule(X,Y,X+8,Y-8),self.blockRule(X,Y,X-8,Y+8),self.blockRule(X,Y,X-8,Y-8)]
        knightChecks = [[self.getPieceAt(X+1,Y+2),X+1,Y+2],[self.getPieceAt(X-1,Y+2),X-1,Y+2]
                        ,[self.getPieceAt(X+1,Y-2),X+1,Y-2],[self.getPieceAt(X-1,Y-2),X-1,Y-2]
                        ,[self.getPieceAt(X+2,Y+1),X+2,Y+1],[self.getPieceAt(X-2,Y+1),X-2,Y+1]
                        ,[self.getPieceAt(X+2,Y-1),X+2,Y-1],[self.getPieceAt(X-2,Y-1),X-2,Y-1]]
        kingChecks = [[self.getPieceAt(X+1,Y+1),X+1,Y+1],[self.getPieceAt(X+1,Y),X+1,Y]
                        ,[self.getPieceAt(X+1,Y-1),X+1,Y-1],[self.getPieceAt(X-1,Y),X-1,Y]
                        ,[self.getPieceAt(X-1,Y+1),X-1,Y+1],[self.getPieceAt(X,Y-1),X,Y-1]
                        ,[self.getPieceAt(X-1,Y-1),X-1,Y-1],[self.getPieceAt(X,Y+1),X,Y+1]]
        blackPawnChecks = [[self.getPieceAt(X-1,Y+1),X-1,Y+1],[self.getPieceAt(X+1,Y+1),X+1,Y+1],[self.getPieceAt(X,Y+1),X,Y+1],[self.getPieceAt(X,Y+2),X,Y+2]]
        whitePawnChecks = [[self.getPieceAt(X-1,Y-1),X-1,Y-1],[self.getPieceAt(X+1,Y-1),X+1,Y-1],[self.getPieceAt(X,Y-1),X,Y-1],[self.getPieceAt(X,Y-2),X,Y-2]]
        for check in straightChecks:
            if (check[0] == 9 or  check[0] == 7) and attackerIsWhite:
                attackers.append(check)
            if (check[0] == 10 or  check[0] == 8) and not attackerIsWhite:
                attackers.append(check)
        for check in diagonalChecks:
            if (check[0] == 9 or  check[0] == 5) and attackerIsWhite:
                attackers.append(check)
            if (check[0] == 10 or  check[0] == 6) and not attackerIsWhite:
                attackers.append(check)
        for check in knightChecks:
            if (check[0] == 3) and attackerIsWhite:
                attackers.append(check)
            if (check[0] == 4)  and not attackerIsWhite:
                attackers.append(check)
        for check in kingChecks:
            if (check[0] == 11) and attackerIsWhite:
                attackers.append(check)
            if (check[0] == 12)  and not attackerIsWhite:
                attackers.append(check)
        if(attackerIsWhite):
            if (piece == 0):
                if (whitePawnChecks[2][0] != 0):
                    if (whitePawnChecks[2][0] == 1):
                        attackers.append(whitePawnChecks[2])
                elif (blackPawnChecks[3][0]==1 and Y == 4):
                    attackers.append(whitePawnChecks[2])
            else:
                if (blackPawnChecks[0][0] == 1):
                    attackers.append(whitePawnChecks[0])
                if (blackPawnChecks[1][0] == 1):
                    attackers.append(whitePawnChecks[1])
        if(not attackerIsWhite):
            if (piece == 0):
                if (blackPawnChecks[2][0] != 0):
                    if (blackPawnChecks[2][0] == 2):
                        attackers.append(blackPawnChecks[2])
                elif (blackPawnChecks[3][0]==2 and Y == 3):
                    attackers.append(blackPawnChecks[2])
            else:
                if (blackPawnChecks[0][0] == 2):
                    attackers.append(blackPawnChecks[0])
                if (blackPawnChecks[1][0] == 2):
                    attackers.append(blackPawnChecks[1])
        return attackers
    

    def offerMove(self,whitesMove,x,y,X,Y):
        print("x: ",x,"y: ",y, "X: ",X,"Y: ",Y)
        attacker = self.getPieceAt(x,y)
        defender = self.getPieceAt(X,Y)
        
        #The Rules begin here, either a rule is violated and returns false, or move is made and returns true.
        if (whitesMove != attacker%2):
            return False
        if (attacker == 0):
            return False
        if (attacker%2 == defender%2 and defender != 0):
            return False
        
        #Movement Rules
        if (attacker == 1):
            if (defender == 0):
                if (y == 3 and X == self.enPass and Y == 2 and (x == X-1 or x == X+1)):
                    self.removePieceAt(X,Y+1)
                else:
                    if (x != X):
                        return False
            self.enPass = None
            if (defender != 0 and (x != X+1 and x != X-1) and y != Y-1):
                return False
            if (y != 6 and Y != y-1):
                return False
            if (y == 6):
                if (Y != 4 and Y !=5):
                    return False
                self.enPass = x
            if (Y == 0):
                self.needsPromotionAt = X
        if (attacker == 2):
            if (defender == 0):
                if (y == 4 and X == self.enPass and Y == 5 and (x == X-1 or x == X+1)):
                    self.removePieceAt(X,Y-1)
                else:
                    if (x != X):
                        return False
            self.enPass = None
            if (defender != 0 and (x != X+1 and x != X-1) and y != Y+1):
                return False
            if (y != 1 and Y != y+1):
                return False
            if (y == 1):
                if (Y != 2 and Y !=3):
                    return False
                self.enPass = x
            if (Y == 7):
                self.needsPromotionAt = X
        if (attacker != 1 and attacker != 2):
            self.enPass = None
        if (attacker == 3 or attacker == 4):
            if ([x,y] != [X+1,Y+2] and [x,y] != [X+1,Y-2] and [x,y] != [X-1,Y+2] and [x,y] != [X-1,Y-2] and [x,y] != [X+2,Y+1] and [x,y] != [X+2,Y-1] and [x,y] != [X-2,Y+1] and [x,y] != [X-2,Y-1]):
                return False
        else:
            if (self.blockRule(x,y,X,Y)[0]) != 0:
                return False
        if (attacker == 5 or attacker == 6):
            if (abs(x - X) != abs(y - Y)):
                return False
        if (attacker == 7 or attacker == 8):
            if (x != X and y != Y):
                return False
        if (attacker == 9 or attacker == 10):
            if ((x != X and y != Y) and (abs(x - X) != abs(y - Y))):
                return False
        if (attacker == 11 or attacker == 12):
            if (abs(x - X) > 1 or abs(y-Y) > 1):
                return False
        return True
    def tryMove(self,whitesMove,x,y,X,Y):
        if(self.offerMove(whitesMove,x,y,X,Y)):
            self.placePieceAt(self.getPieceAt(x,y),X,Y) 
            self.removePieceAt(x,y)
            return True
        else:
            return False
    def simulateValidMove(self, x, y, X, Y, isWhite):
        result = True
        piece = self.getPieceAt(x,y)
        targetPiece = self.getPieceAt(X,Y)
        
        self.placePieceAt(piece,X,Y) 
        self.removePieceAt(x,y)

        if (isWhite):
            if (len(self.whiteKingChecks()) > 0):
                result = False
        else:
            if (len(self.blackKingChecks()) > 0):
                result = False
        self.placePieceAt(piece,x,y)
        self.placePieceAt(targetPiece,X,Y)

        return result


class GameController:
    def __init__(self):
        self.playGame = True
        self.gameMode = 'menu'
        self.whitesMove = True
        self.selected = False
        self.selectedX = 0
        self.selectedY = 0
        self.editPieces = [[1,3,5,7,9,11],[2,4,6,8,10,12]]
        self.editWithPiece = 0

        self.GM = GameModel()
        self.GV = GameView(self.GM,self)
        self.GV.win.bind("<Button-1>", self.onClick)
        self.GV.win.pack()
        self.GV.updateScreen()
        while(self.playGame):
            self.GV.view.update()
    def regularTurn(self, positionX, positionY):
        
        if (positionX > 7):
            if (positionY == 7):
                self.GV.buttonOutline(8)
                self.gameMode = 'menu'

        else:
            if (self.whitesMove):
                if (self.selected):
                    if (self.GM.tryMove(self.whitesMove,self.selectedX,self.selectedY,positionX,positionY)):
                        print(self.GM.needsPromotionAt)
                        if(self.GM.needsPromotionAt != None):
                            self.GM.doPromotionAt(True, self.GV.promotePrompt())
                        self.GV.updateScreen()
                        time.sleep(1)
                        self.whitesMove = False
                    self.selected = False
                
                else:
                    self.selected = True
                    self.selectedX = positionX
                    self.selectedY = positionY
            else:
               if (self.selected):
                    if (self.GM.tryMove(self.whitesMove,7-self.selectedX,7-self.selectedY,7-positionX,7-positionY)):
                        if(self.GM.needsPromotionAt != None):
                            self.GM.doPromotionAt(False, self.GV.promotePrompt())                    
                        self.GV.updateScreen()
                        time.sleep(1)
                        self.whitesMove = True
                    self.selected = False
               else:
                    self.selected = True
                    self.selectedX = positionX
                    self.selectedY = positionY

    def menuSelection(self,positionX,positionY):
        if (positionX > 7):
            if (positionY == 7):
                self.GV.buttonOutline(8)
                self.playGame = False
            if (positionY == 1):
                self.GV.buttonOutline(2)
                self.gameMode = 'edit'
            if (positionY == 0):
                self.GV.buttonOutline(1)
                self.GM.setUpBoard(self.GM.initBoardData)
                self.gameMode = 'play'
    def editSelection(self,positionX,positionY):
        if(positionX>7):
            if (positionY > 0 and positionY <7):
                if (self.selected and (self.selectedX == positionX and self.selectedY == positionY)):
                    self.selected = False
                    self.selectedX = 0
                    self.selectedY = 0
                    self.editWithPiece = 0
                else:
                    self.selected = True
                    self.selectedX = positionX
                    self.selectedY = positionY
                    self.editWithPiece = self.editPieces[positionX-8][positionY-1]
            if (positionY == 0):
                self.GV.buttonOutline(1)
                self.gameMode = 'play'
            if (positionY == 7):
                self.GV.buttonOutline(8)
                self.gameMode = 'menu'

        else:
            self.GM.placePieceAt(self.editWithPiece,positionX,positionY)



    def onClick(self,event):
        #print("at start: ", self.GM.enPass)
        positionX = int(event.x/self.GV.Tsize)
        positionY = int(event.y/self.GV.Tsize)
        
        if (self.gameMode == 'play'):
            self.regularTurn(positionX,positionY)
            self.GV.updateScreen()
        elif (self.gameMode == 'menu'):
            self.menuSelection(positionX,positionY)
            self.GV.updateScreen()
        elif (self.gameMode == 'edit'):
            self.editSelection(positionX,positionY)
            self.GV.updateScreen()

        #print("at end: ", self.GM.enPass)
class TestGameModel(unittest.TestCase):
    
    def test_unitTest(self):
        self.GM = GameModel()
        print(self.GM.squareAttackers(3,1,False))

#unittest.main()
GC = GameController()



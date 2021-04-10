#from graphics import *
from tkinter import *
import time
import numpy


class GameView:

    def __init__(self,model):
        self.fileList = ["Pawn_W.png","Pawn_B.png","Knight_W.png","Knight_B.png","Bishop_W.png","Bishop_B.png","Rook_W.png","Rook_B.png","Queen_W.png","Queen_B.png","King_W.png","King_B.png"]
        self.view = Tk()
        self.Tsize = 50
        self.winW = self.Tsize*8
        self.winH = self.Tsize*8
        self.modW = self.Tsize*2
        self.model = model
        self.win = Canvas(self.view, width = self.winW, height = self.winH)
        self.win.pack()
        self.imageList = [PhotoImage(file="C:\\Users\\Ethan\\Source\Repos\\Chess-Python\\Graphics\\" + i) for i in self.fileList]
        self.boardImage = PhotoImage(file="C:\\Users\\Ethan\\Source\Repos\\Chess-Python\\Graphics\\" + "ChessBoard.png")
    
    def placePiece(self,piece, x, y):
        if (piece>0):
            self.win.create_image(x-25,y-25,image = self.imageList[piece-1])
        
    
    def updateScreen(self): 
        self.win.delete('all')
        self.win.create_image(self.winW/2,self.winH/2, image = self.boardImage)
        for x in range(8):
            for y in range(8):
                self.placePiece(self.model.getPieceAt(x,y),(x+1)*self.Tsize,(y+1)*self.Tsize)
        self.win.update()
        


class GameModel:
    def __init__(self):
        initBoardData = [[8,4,6,10,12,6,4,8],[2,2,2,2,2,2,2,2],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[7,3,5,9,11,5,3,7]]
        self.boardData = numpy.array(initBoardData)
    def getPieceAt(self,x,y):
        return self.boardData[y,x]
    def removePieceAt(self,x,y):
        self.boardData[y,x] = 0
    def placePieceAt(self,piece, x, y):
        self.boardData[y,x] = piece

class GameController:
    def __init__(self):
        self.whitesMove = True






GM = GameModel()
GV = GameView(GM)
GM.removePieceAt(0,0)
GM.placePieceAt(3,1,0)
GV.updateScreen()
time.sleep(2)
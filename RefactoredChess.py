#from graphics import *
from tkinter import *
import time
import numpy


class GameView:
    def __init__(self,model,controller):
        self.fileList = ["Pawn_W.png","Pawn_B.png","Knight_W.png","Knight_B.png","Bishop_W.png","Bishop_B.png","Rook_W.png","Rook_B.png","Queen_W.png","Queen_B.png","King_W.png","King_B.png","tile_khaki.png","tile_pink.png"]
        self.view = Tk()
        self.Tsize = 50
        self.winW = self.Tsize*8
        self.winH = self.Tsize*8
        self.modW = self.Tsize*2
        self.model = model
        self.controller = controller
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
        self.placeSpecialTiles()
        
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
        if (self.controller.selected):
            self.placePiece(13,(self.controller.selectedX+1)*self.Tsize,(self.controller.selectedY+1)*self.Tsize)



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
    def offerMove(self,x,y,X,Y):
        self.placePieceAt(self.getPieceAt(x,y),X,Y) 
        self.removePieceAt(x,y)
        return True


class GameController:
    def __init__(self):
        self.whitesMove = True
        self.selected = False
        self.selectedX = 0
        self.selectedY = 0

        self.GM = GameModel()
        self.GV = GameView(self.GM,self)
        self.GV.win.bind("<Button-1>", self.onClick)
        self.GV.win.pack()
        self.GV.updateScreen()
        self.GV.view.mainloop()
        
    def onClick(self,event):
        
        positionX = int(event.x/self.GV.Tsize)
        positionY = int(event.y/self.GV.Tsize)
        if (self.whitesMove):
            if (self.selected):
                if (self.GM.offerMove(self.selectedX,self.selectedY,positionX,positionY)):
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
                if (self.GM.offerMove(7-self.selectedX,7-self.selectedY,7-positionX,7-positionY)):
                    self.GV.updateScreen()
                    time.sleep(1)
                    self.whitesMove = True
                self.selected = False
           else:
                self.selected = True
                self.selectedX = positionX
                self.selectedY = positionY
        self.GV.updateScreen()
        

        
        



GC = GameController()

#GM.removePieceAt(0,0)
#GM.placePieceAt(3,1,0)
#GV.updateScreen()
#time.sleep(2)
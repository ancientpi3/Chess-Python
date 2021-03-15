from graphics import *
import time
import tkinter
Tsize = 50
winW = Tsize*8
winH = Tsize*8
modW = Tsize*2
win = GraphWin("Chess", winW + modW, winH)

while 0:
    print(1)





mouseX = 0
mouseY = 0
EnPasOn = None
isswitched = False
BkingSideMoved = False
BqueenSideMoved = False
WkingSideMoved = False
WqueenSideMoved = False
QCastle = False
KCastle = False
DoPromotion = False
EP = True
QCastle = False
KCastle = False
Promote = False
UpdateBoardData = True
posX = None
posY = None
movX = None
movY = None
PcAttacked = None
PcSelected = None
firstPlace = False
WKcheck = False
BKcheck = False
CurrentMode="Menu"

initBoardData = [[8,4,6,10,12,6,4,8],[2,2,2,2,2,2,2,2],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[7,3,5,9,11,5,3,7]]

BoardData = initBoardData
piecesFile = ["Pawn_W.png","Pawn_B.png","Knight_W.png","Knight_B.png","Bishop_W.png","Bishop_B.png","Rook_W.png","Rook_B.png","Queen_W.png","Queen_B.png","King_W.png","King_B.png"]

def PlaceTile(x,y,tile):
    if (tile == "wht"):
        t = Image(Point(x+25,y+25),"C:\\Users\\Ethan\\Documents\\Chess_1\\"+"tile_bisque.png")
    if (tile == "blc"):
        t = Image(Point(x+25,y+25),"C:\\Users\\Ethan\\Documents\\Chess_1\\"+"tile_sienna.png")
    if (tile == "slct"):
        t = Image(Point(x+25,y+25),"C:\\Users\\Ethan\\Documents\\Chess_1\\"+"tile_khaki.png")
    if (tile == "chck"):
        t = Image(Point(x+25,y+25),"C:\\Users\\Ethan\\Documents\\Chess_1\\"+"tile_pink.png")
    if (tile == "play"):
        t = Image(Point(x+50,y+25),"C:\\Users\\Ethan\\Documents\\Chess_1\\"+"playbutt.png")
    if (tile == "exit"):
        t = Image(Point(x+50,y+25),"C:\\Users\\Ethan\\Documents\\Chess_1\\"+"exitbutt.png")
    if (tile == "edit"):
        t = Image(Point(x+50,y+25),"C:\\Users\\Ethan\\Documents\\Chess_1\\"+"editbutt.png")
    if (tile == "back"):
        t = Image(Point(x+50,y+25),"C:\\Users\\Ethan\\Documents\\Chess_1\\"+"backbutt.png") 
    t.draw(win)
def PlacePiece(x,y,pieceNum,doDraw):
    if (pieceNum !=0):
        p = Image(Point(x+24,y+24),"C:\\Users\\Ethan\\Documents\\Chess_1\\"+piecesFile[pieceNum-1])
    if (pieceNum == 0):
        X = x/Tsize
        Y = y/Tsize    
        if ((X+Y)%2 == 0):
            PlaceTile(x,y,"wht")
            
        else:
            PlaceTile(x,y,"blc")
            
    else:
        if doDraw == True:
            p.draw(win)
        else:
            p.undraw()
def CreateBoard():
    win.delete('all')
    b = Image(Point(winH/2,winW/2),"C:\\Users\\Ethan\\Documents\\Chess_1\\ChessBoard.png")
    m = Image(Point(winH+50,winW/2),"C:\\Users\\Ethan\\Documents\\Chess_1\\sideMod.png")
    b.draw(win)
    m.draw(win)
    #for x in range(0,8,1):
        #for y in range(0,8,1):
            #if ((x+y)%2 == 0):
                #PlaceTile((x)*Tsize,(y)*Tsize,"wht")
            #else:
                #PlaceTile((x)*Tsize,(y)*Tsize,"blc")
                

def ResetPieces():
    for y in range(0,8,1):
        for x in range(0,8,1): 
            PlacePiece(x*Tsize,y*Tsize,initBoardData[y][x],True)
def LoadPieces():
    if isswitched:
        for y in range(0,8,1):
            for x in range(0,8,1): 
                PlacePiece(x*Tsize,y*Tsize,BoardData[7-y][7-x],True)
    else:
        for y in range(0,8,1):
            for x in range(0,8,1): 

                PlacePiece(x*Tsize,y*Tsize,BoardData[y][x],True)





def DoEnPassant():
    global BoardData
    print("Enpass Done")
    UpdateBoardData = False
    if isswitched:
        BoardData[7-posY][7-posX] = 0
        BoardData[7-movY-1][7-movX] = 0
        BoardData[7-movY][7-movX] = 2
    else:
        BoardData[posY][posX] = 0
        BoardData[movY+1][movX] = 0
        BoardData[movY][movX] = 1



def ValidMove():
    global BoardData
    global QCastle
    global KCastle
    global DoPromotion
    global UpdateBoardData
    global EnPasOn
    if (PcAttacked != 0):
        if (PcSelected%2 == PcAttacked%2):
            return False


    if isswitched:
        if (PcSelected%2 != 0):
            
            return False
    else:
        if (PcSelected%2 == 0):
            
            return False





        
 
     

        
        
    if (PcSelected == 1) or (PcSelected == 2):
        if (EnPasOn != None):
            if  PcAttacked == 0 and (([movX,movY] == [posX+1,posY-1] and movX == (7-EnPasOn) and movY == 2) or ([movX,movY] == [posX-1,posY-1] and movX == (7-EnPasOn) and movY == 2)):
                DoEnPassant()
                return True
        if ([movX,movY] == [posX,posY-1] and PcAttacked == 0) or (posY == 6 and [movX,movY] == [posX,posY-2] and PcAttacked == 0) or PcAttacked != 0 and ([movX,movY] == [posX+1,posY-1] or [movX,movY] == [posX-1,posY-1]):
            if movY == 0:
                DoPromotion = True
                UpdateBoardData = False
            if (posY == 6 and [movX,movY] == [posX,posY-2]):
                EnPasOn = movX
                EP = isswitched
                #print("En Passant can Happen on X = ", 7-EnPasOn)
            return True
        else:    
            return False




    if (PcSelected == 3) or (PcSelected == 4):
        if [posX,posY] == [movX+2,movY-1] or [posX,posY] == [movX-2,movY-1] or [posX,posY] == [movX-2,movY+1] or [posX,posY] == [movX+2,movY+1] or [posX,posY] == [movX+1,movY-2] or [posX,posY] == [movX-1,movY-2] or [posX,posY] == [movX-1,movY+2] or [posX,posY] == [movX+1,movY+2]:
            return True
        else:
            return False

    if (PcSelected == 5) or (PcSelected == 6):
        if (abs(posX - movX) == abs(posY - movY)):
            return True
        else:
            return False


    if (PcSelected == 7) or (PcSelected == 8):
        if (posX == movX) and (posY != movY) or (posX !=movX) and (posY == movY):
            return True
        else:
            return False
    if (PcSelected == 9) or (PcSelected == 10):
        if (abs(posX - movX) == abs(posY - movY)) or ((posX == movX) and (posY != movY) or (posX !=movX) and (posY == movY)):
            return True
        else:
            return False
    if (PcSelected == 11) or (PcSelected == 12):
        if abs(posX-movX) == 1 or abs(posY-movY) == 1:
            return True
        else:
            
            
            if (PcSelected == 11) and [movX,movY] == [6,7] and WkingSideMoved == False:
                KCastle = True
                return True
            if (PcSelected == 12) and [movX,movY] == [1,7] and BkingSideMoved == False:
                KCastle = True
                return True
            if (PcSelected == 11) and [movX,movY] == [2,7] and WqueenSideMoved == False:
                QCastle = True
                return True
            if (PcSelected == 12) and [movX,movY] == [5,7] and BqueenSideMoved == False:
                QCastle = True
                return True
            return False
    
    return True
def CheckForNoCastle():
    global WqueenSideMoved
    global WkingSideMoved
    global BqueenSideMoved
    global BkingSideMoved
    if BoardData[7][4] != 11 or BoardData[7][0] != 7:
        WqueenSideMoved = True
    if BoardData[7][4] != 11 or BoardData[7][7] != 7:
        WkingSideMoved = True
    if BoardData[0][4] != 12 or BoardData[0][7] != 8:
        BqueenSideMoved = True
    if BoardData[0][4] != 12 or BoardData[0][0] != 8:
        BkingSideMoved = True
        
def Block():
    if (PcSelected != 3) and (PcSelected != 4):
        
        
        if (posX == movX) and (posY != movY):
            yStep = int(abs(movY-posY)/(movY-posY))
            
            for y in range(posY+yStep,movY, yStep):
                
                if isswitched:
                    if (BoardData[7-y][7-posX] != 0):
                        return False
                else:
                    if (BoardData[y][posX] != 0):
                        return False
        if (posY ==  movY) and (posX != movX):
            xStep = int(abs(movX-posX)/(movX-posX))
            
            
            for x in range(posX+xStep,movX, xStep):
                if isswitched:
                    if (BoardData[7-posY][7-x] != 0):
                        return False
                else:
                    if (BoardData[posY][x] != 0):
                        return False
        
        if (posY != movY) and (posX != movX):
            xStep = int(abs(movX-posX)/(movX-posX))
            yStep = int(abs(movY-posY)/(movY-posY))
            x = posX
            for y in range(posY+yStep,movY, yStep):
                x = x + xStep
                if isswitched:
                    if (BoardData[7-y][7-x] != 0):
                        return False
                else:
                    if (BoardData[y][x] != 0):
                        return False
        return True
    else:
        return True


def PromoteButton():
    button = tkinter.Tk()
    
    def Queen():
        global BoardData
        if isswitched:
            BoardData[7-posY][7-posX] = 0
            BoardData[7-movY][7-movX] = 10
        else:
            BoardData[posY][posX] = 0
            BoardData[movY][movX] = 9
        button.quit()
        button.destroy()
    def Rook():
        global BoardData
        if isswitched:
            BoardData[7-posY][7-posX] = 0
            BoardData[7-movY][7-movX] = 8
        else:
            BoardData[posY][posX] = 0
            BoardData[movY][movX] = 7
        button.quit()
        button.destroy()
    def Bishop():
        global BoardData
        if isswitched:
            BoardData[7-posY][7-posX] = 0
            BoardData[7-movY][7-movX] = 6
        else:
            BoardData[posY][posX] = 0
            BoardData[movY][movX] = 5
        button.quit()
        button.destroy()
    def Knight():
        global BoardData
        if isswitched:
            BoardData[7-posY][7-posX] = 0
            BoardData[7-movY][7-movX] = 4
        else:
            BoardData[posY][posX] = 0
            BoardData[movY][movX] = 3
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
#variable clr is 1 for white and 0 for black
def CheckAttack(x,y,clr,BoardData3):
    NumberOfChecks = 0
    Ksteps = [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
    for k in range(0,8):
        
        X = x + Ksteps[k][0]
        Y = y + Ksteps[k][1]
        #print("searching: ",X," ",Y)
        if (X) <= 7 and (Y) <= 7 and (X) >= 0 and (Y) >= 0:
            Pc = BoardData3[Y][X]
            #print("in range: ",X," ",Y)
            if (Pc == 3 and clr == 1) or (Pc == 4 and clr == 0):
                NumberOfChecks+=1
                print("Knight Checking ", Pc)
                
                
    for Xstep in range(-1,2):
        for Ystep in range(-1,2):
            #print("step: ",Xstep,Ystep)
            Stop = False
            if (Xstep,Ystep) != (0,0):
                #print("test 2")
                
                    #print("test 3")
                if (x+Xstep) <= 7 and (y+Ystep) <= 7 and (x+Xstep) >= 0 and (y+Ystep) >= 0:
                    Pc = BoardData3[y+Ystep][x+Xstep]
                    if (Pc == 11 and clr == 1) or (Pc == 12 and clr == 0):
                        NumberOfChecks+=1
                        print("King Checking", Pc)
                        Stop = True                        
                    if abs(Xstep*Ystep)==1:
                        if (clr == 1) and (Pc == 2) and (Ystep == -1):
                            NumberOfChecks+=1
                            print("Pawn Checking", Pc)
                            Stop = True
                        if (clr == 0) and (Pc == 1) and (Ystep == 1):
                            NumberOfChecks+=1
                            print("Pawn Checking", Pc)
                            Stop = True
                X =x
                Y =y
                #print("reset coord")
                while Stop==False:
                    #print("test 4")
                    X = X+Xstep
                    Y = Y+Ystep
                    #print("coord: ",X,Y,Xstep,Ystep)
                    
                    if X <= 7 and Y <= 7 and X >= 0 and Y >= 0:
                        Pc = BoardData3[Y][X]
                        if Pc is not 0:
                            if Pc%2 == clr:
                                #print("this square has a clr piece on it")
                                Stop = True
                            else:
                                if (abs(Ystep*Xstep)==1) and (Pc == 5 or Pc == 6 or Pc == 9 or Pc == 10):
                                    NumberOfChecks+=1
                                    print("Bishops or Queen Checking", Pc)
                                    
                                    #print("Bishop Test")
                                if (abs(Ystep*Xstep)==0) and (Pc == 7 or Pc == 8 or Pc == 9 or Pc == 10):
                                    NumberOfChecks+=1
                                    print("Rook or Queen Checking", Pc)
                            Stop = True        
                                #print("nop")
                                
                    else:
                        #print("end of stop loop")
                        Stop = True
    return NumberOfChecks

def CheckForCheck(clr,BoardData2):
    for x in range(0,8):
        for y in range (0,8):
            if BoardData2[y][x] == (12 - clr):
                if CheckAttack(x,y,clr,BoardData2):
                    return True
                else:
                    return False
def SimulateCheck(isswitched,SimBoardData):
    global WKcheck
    global BKcheck
    if isswitched:
        clr = 0
    else:
        clr = 1
    if isswitched:
        SimBoardData[7-posY][7-posX] = 0
        SimBoardData[7-movY][7-movX] = PcSelected
        if(QCastle):
            SimBoardData[0][0] = 0
            SimBoardData[0][3] = 8
        if(KCastle):          
            SimBoardData[0][7] = 0
            SimBoardData[0][5] = 8
    else:
        SimBoardData[posY][posX] = 0
        SimBoardData[movY][movX] = PcSelected
        if(QCastle):
            SimBoardData[7][0] = 0
            SimBoardData[7][3] = 7
        if(KCastle):             
            SimBoardData[7][7] = 0
            SimBoardData[7][5] = 7
    for x in range(0,8):
        for y in range (0,8):
            if SimBoardData[y][x] == (11 + clr):
                return CheckAttack(x,y,clr,SimBoardData)
                    
                    
            

def EditorMode():
    global BoardDataSave
    global BoardData
    global CurrentMode
    global isswitched
    isswitched = False
    def loadEditMod():
        PlaceTile(8*50,0*50,"play")
        PlaceTile(8*50,7*50,"back")
        for x in range(8,10):
            for y in range(1,7):
                if [x-7,y] == buttSelect:
                    PlaceTile(x*50,y*50,"slct")
                    PlacePiece(x*50,y*50,2*y-(9-x),True)
                else:
                    PlacePiece(x*50,y*50,2*y-(9-x),True)
    Selection = False

    BoardData = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    CreateBoard()
    #ResetPieces()
    PSelected = 1
    buttSelect = [1,1]
    loadEditMod()
    
    while CurrentMode=="Edit":
        click = win.checkMouse()
        if click != None:
            posX = int(click.getX() / 50)
            posY = int(click.getY() / 50)
            if posX <= 7:
                if BoardData[posY][posX] == 0:
                    BoardData[posY][posX] = PSelected
                else:
                    BoardData[posY][posX] = 0

            else:
                buttSelect = [posX-7,posY]
                if (posY >= 1 and posY <= 6):
                    if buttSelect[0] == 1:
                        PSelected = posY*2 - 1
                    else:
                        PSelected = posY*2
                else:
                    if posY == 0:
                        CurrentMode = "Test"
                    else:
                        CurrentMode = "Menu"
            CreateBoard()           
            LoadPieces()
            loadEditMod()
        
def DoRegularGame():
    global EnPasOn
    global isswitched
    global BkingSideMoved
    global BqueenSideMoved
    global WkingSideMoved
    global WqueenSideMoved
    global QCastle
    global KCastle
    global DoPromotion
    global EP
    global QCastle
    global KCastle
    global Promote
    global UpdateBoardData
    global posX
    global posY
    global movX
    global movY
    global PcAttacked
    global PcSelected
    global CurrentMode
    def loadRegMod():
        PlaceTile(8*50,7*50,"back")
        

    isswitched = False
    global WKcheck
    global BKcheck
    CreateBoard()
    

    
    LoadPieces()
    loadRegMod()



    Selection = False
    while CurrentMode=="Play":


        click = win.getMouse()
        if (Selection == False) and (click != None):
        
        
            posX = int(click.getX() / 50)
            posY = int(click.getY() / 50)
            if posX <=7:
                if isswitched:
                    PcSelected = BoardData[7-posY][7-posX]
                else:
                    PcSelected = BoardData[posY][posX]

                PlaceTile(posX*Tsize, posY*Tsize, "slct")
                PlacePiece(posX*Tsize, posY*Tsize, PcSelected,True)
                click = None

                if (PcSelected == 0):
                    Selection = False 
                else:
                    Selection = True
            else:
                click = None
                if posY == 7:
                    CurrentMode = "Menu"

        
        if (Selection == True) and (click != None):
        
            Selection = False
            movX = int(click.getX() / 50)
            movY = int(click.getY() / 50)
            if movX<=7:
                if isswitched:
                    PcAttacked = BoardData[7-movY][7-movX]
                else:
                    PcAttacked = BoardData[movY][movX]
            else:
                if movY == 7:
                    CurrentMode = "Menu"
        
        
            #
            #
            #
            #
            #
            #
            #
            #
            #

 #           if WKcheck == True:
  #              StillChecked = SimulateCheck(isswitched,BoardData)
   #             WKcheck == False
    #        else:
     #           StillChecked = False
      #      if BKcheck == True:
       #         StillChecked = SimulateCheck(isswitched,BoardData)
        #        BKcheck == False
         #   else:
          #      StillChecked = False

            StillChecked = False
            if ValidMove() and Block() and not StillChecked:

                if EP != isswitched:
                    EnPasOn = None
                
                if UpdateBoardData:
                    
                    if isswitched:
                        clr = 1
                        BoardData[7-posY][7-posX] = 0
                        BoardData[7-movY][7-movX] = PcSelected
                        if(QCastle):
                            BoardData[0][0] = 0
                            BoardData[0][3] = 8
                        if(KCastle):
                            
                            BoardData[0][7] = 0
                            BoardData[0][5] = 8
                    else:
                        clr = 0
                        BoardData[posY][posX] = 0
                        BoardData[movY][movX] = PcSelected
                        if(QCastle):
                            BoardData[7][0] = 0
                            BoardData[7][3] = 7
                        if(KCastle):
                            
                            BoardData[7][7] = 0
                            BoardData[7][5] = 7
                    for x in range(0,8):
                        for y in range (0,8):
                            #if clr == 0:
                            if BoardData[7-y][7-x] == (12):
                                Kx = x
                                Ky = y
                                if CheckAttack(7-x,7-y,0,BoardData):
                                    BKcheck = True
                                else:
                                    BKcheck = False
                                    WKcheck = False

                            #else:
                                
                            if BoardData[7-y][7-x] == (11):
                                Kx = x
                                Ky = y
                                if CheckAttack(7-x,7-y,1,BoardData):
                                    WKcheck = True
                                else:
                                    BKcheck = False
                                    WKcheck = False
                    print(WKcheck)
                    print(BKcheck)
                    print(Kx," ",Ky)
                        
                else:
                    if DoPromotion:
                        PromoteButton()
                        
               
                
                if PcAttacked != 0:
                    if ((movX+movY)%2 == 0):
                        PlaceTile((movX)*Tsize,(movY)*Tsize,"wht")
                    else:
                        PlaceTile((movX)*Tsize,(movY)*Tsize,"blc")
                LoadPieces()
                if WKcheck == True:
                    PlaceTile(Kx*50,Ky*50,"chck")                    
                    PlacePiece(Kx*50,Ky*50,11,True)
                if BKcheck == True:
                    PlaceTile((7-Kx)*50,(7-Ky)*50,"chck")
                    PlacePiece((7-Kx)*50,(7-Ky)*50,12,True)

                                        
                time.sleep(.3)
                #time.sleep(2)
                isswitched = not isswitched

        

                CreateBoard()
                loadRegMod()
                LoadPieces()
                if WKcheck == True:
                    PlaceTile((7-Kx)*50,(7-Ky)*50,"chck")                    
                    PlacePiece((7-Kx)*50,(7-Ky)*50,11,True)
                if BKcheck == True:
                    PlaceTile((Kx)*50,(Ky)*50,"chck")
                    PlacePiece((Kx)*50,(Ky)*50,12,True)
                QCastle = False
                KCastle = False
                CheckForNoCastle()
                UpdateBoardData = True
                
            else:
                QCastle = False
                KCastle = False
                Selection = False
                PlacePiece(posX*Tsize, posY*Tsize, 0,True)
                PlacePiece(posX*Tsize, posY*Tsize, PcSelected,True)
def CheckTest():
    global CurrentMode
    while CurrentMode == "Test":
        clr = 1
 #       for Kx in range(0,8):
  #          for y in range (0,8):
   #             if BoardData[y][x] == (12 - clr):
    #                if CheckAttack(x,y,clr,BoardData):
     #                   PlaceTile(x*50,y*50,"chck")
      #                  PlacePiece(x*50,y*50,12 - clr,True)
       #                 if clr == 1:
        #                    WKcheck = True
         #                   BKcheck = False
          #              else:
           #                 BKcheck = True
            #                WKcheck = False
                                
        
        click = win.getMouse()
        if (click != None):
            CurrentMode = "Edit"
            
    
        



        for posY in range(0,8):
            print(CheckAttack(0,posY,clr,BoardData),CheckAttack(1,posY,clr,BoardData),CheckAttack(2,posY,clr,BoardData),CheckAttack(3,posY,clr,BoardData),CheckAttack(4,posY,clr,BoardData),CheckAttack(5,posY,clr,BoardData),CheckAttack(6,posY,clr,BoardData),CheckAttack(7,posY,clr,BoardData))
        click = win.getMouse()
        if (click != None):
            CurrentMode = "Edit"
            
        
def MenuMode():
    def loadMenuMod():
        PlaceTile(8*50,0*50,"play")
        PlaceTile(8*50,1*50,"edit")
        PlaceTile(8*50,7*50,"exit")
    global CurrentMode
    global BoardData
    CreateBoard()
    loadMenuMod()
    
    while CurrentMode == "Menu":
        click = win.getMouse()
        posX = int(click.getX() / 50)
        posY = int(click.getY() / 50)
        if posX >=8:
            if posY == 0:
                BoardData = initBoardData
                CurrentMode = "Play"
            if posY == 1:
                CurrentMode = "Edit"
            if posY == 7:
                CurrentMode = "Exit"

    



Game=True
while Game:
    if CurrentMode=="Menu":
        MenuMode()
    if CurrentMode=="Play":
        DoRegularGame()
    if CurrentMode=="Edit":
        EditorMode()
    if CurrentMode=="Exit":
        Game=False
    if CurrentMode=="Test":
        CheckTest()
        Game=False
win.close()











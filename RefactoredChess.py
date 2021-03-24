import pygame
import time
import numpy










class GameView:
    fileList = ["Pawn_W.png","Pawn_B.png","Knight_W.png","Knight_B.png","Bishop_W.png","Bishop_B.png","Rook_W.png","Rook_B.png","Queen_W.png","Queen_B.png","King_W.png","King_B.png"]
    for i in fileList:
        imageList = imagelist + [pygame.image.load(os.path.join('data', i))]
    
    Tsize = 50
    winW = Tsize*8
    winH = Tsize*8
    modW = Tsize*2

    WIN = pygame.display.set_mode((winH,winW))
    pygame.display.set_caption("Chess")
class GameModel:
    initBoardData = [[8,4,6,10,12,6,4,8],[2,2,2,2,2,2,2,2],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[7,3,5,9,11,5,3,7]]
    boardData = numpy.array(initBoardData)

class GameController:
    def main():
        clock = pygame.time.Clock()
        run = True;
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False






        pygame.quit()
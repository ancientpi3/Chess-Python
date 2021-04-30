from tkinter import *
import time
fileList = ["Pawn_W.png","Pawn_B.png","Knight_W.png","Knight_B.png","Bishop_W.png","Bishop_B.png","Rook_W.png","Rook_B.png","Queen_W.png","Queen_B.png","King_W.png","King_B.png"]
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
#canvas.pack()      
#img = PhotoImage(file="C:\\Users\\Ethan\\Source\Repos\\Chess-Python\\Graphics\\"+fileList[1])      
#canvas.create_image(20,20, anchor=NW, image=img)      
#root.update()
#time.sleep(1)


def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    print ("clicked at",5%2, event.x, event.y)

#canvas= Canvas(root, width=100, height=100)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()

#root.mainloop
def series1():
    sum = 0
    for n in range(1,100000):
        sum = sum+(1/n)
    return sum
def series2():
    sum = 0
    for n in range(1,100000):
        sum = sum+((1/n)*(-1)**n)
    return sum

for i in range(1,2):
    print("yuk")


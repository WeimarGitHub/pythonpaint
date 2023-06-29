# Python Raster Graphics Editor: Source Code
from turtle import *
t1 = Turtle()
t1.speed(10)
scr = t1.getscreen()
      
def undo():
    t1.undo() 

def move(x, y):
    t1.penup()
    t1.shape('arrow')
    t1.goto(x, y)
    t1.pendown()

def draw(x, y):
    t1.goto(x, y)

def changeBlue():
    t1.color('blue')
    t1.width(1)

def goUp():
    x = t1.xcor()
    y = t1.ycor()
    t1.goto(x, y+3)

def goDown():
    x = t1.xcor()
    y = t1.ycor()
    t1.goto(x, y-3)

def goRight():
    x = t1.xcor()
    y = t1.ycor()
    t1.goto(x+3, y)

def goLeft():
    x = t1.xcor()
    y = t1.ycor()
    t1.goto(x-3, y)

def changeRed():
    t1.color('red')
    t1.width(1)

def changeYellow():
    t1.color('yellow')
    t1.width(1)

def changeCyan():
    t1.color('cyan')
    t1.width(1)

def changeMagenta():
    t1.color('magenta')
    t1.width(1)

def changeGreen():
    t1.color('darkGreen')
    t1.width(1)

def changeOrange():
    t1.color('orange red')
    t1.width(1)

def changeBrown():
    t1.color('saddle brown')
    t1.width(1)

def changeBlack():
    t1.color('black')
    t1.width(1)

def changeGray():
    t1.color('gray')
    t1.width(1)

def changePurple():
    t1.color('purple')
    t1.width(1)

def changeGold():
    t1.color('gold')
    t1.width(1)

def changeOlive():
    t1.color('olive')
    t1.width(1)

def changeTeal():
    t1.color('sea green')
    t1.width(1)

def changeRainbow():
    for i in range(100):
        t1.color('red')
        t1.color('orange')
        t1.color('yellow')
        t1.color('green')
        t1.color('blue')
        t1.color('purple')
        t1.color('pink')
        t1.color('saddle brown')
        t1.color('grey')
        t1.color('black')

def eraser():
    t1.color('white')
    t1.width(15)

scr.onclick(move)
t1.ondrag(draw)
scr.listen()
scr.onkey(t1.clear, 'x')
scr.onkey(changeBlue,'b')
scr.onkey(goUp,'Up')
scr.onkey(goDown,'Down')
scr.onkey(goRight,'Right')
scr.onkey(goLeft,'Left')
scr.onkey(changeCyan,'c')
scr.onkey(changeYellow,'y')
scr.onkey(changeRed,'r')
scr.onkey(changeMagenta,'m')
scr.onkey(changeGreen,'g')
scr.onkey(changeRainbow,'w')
scr.onkey(changeOrange,'o')
scr.onkey(changeBrown,'d')
scr.onkey(changeBlack,'k')
scr.onkey(changeGray,'t')
scr.onkey(changePurple,'p')
scr.onkey(changeGold,'v')
scr.onkey(changeOlive,'h')
scr.onkey(eraser,'e')
scr.onkey(undo, 'u')

scr.mainloop()

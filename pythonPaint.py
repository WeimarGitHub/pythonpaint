from turtle import *
t1 = Turtle()
t1.speed(10)
scr = t1.getscreen()

def move(x, y):
    t1.penup()
    t1.shape('turtle')
    t1.goto(x, y)
    t1.pendown()

def draw(x, y):
    t1.goto(x, y)

def changeBlue():
    t1.color('blue')

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

def changeYellow():
    t1.color('yellow')

def changeCyan():
    t1.color('cyan')

def changeMagenta():
    t1.color('magenta')

def changeGreen():
    t1.color('darkGreen')

def changeOrange():
    t1.color('orange red')

def changeBrown():
    t1.color('saddle brown')

def changeBlack():
    t1.color('black')

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

scr.mainloop()

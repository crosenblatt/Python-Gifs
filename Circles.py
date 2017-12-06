import graphics
import math

win = graphics.GraphWin("Graphics Window", 500, 500)

pt0 = graphics.Point(275, 250)
pt30 = graphics.Point(250 + 40 * math.cos(math.pi/6), 250 - 40 * math.sin(math.pi/6))
pt60 = graphics.Point(250 + 60 * math.cos(math.pi/3), 250 - 60 * math.sin(math.pi/3))
pt90 = graphics.Point(250, 200)
pt120 = graphics.Point(250 - (30 * math.cos(math.pi/3)), 250 - (30 * math.sin(math.pi/3)))
pt150 = graphics.Point(250, 250)


cir = graphics.Circle(pt0, 5)
cir2 = graphics.Circle(pt30, 5)
cir3 = graphics.Circle(pt60, 5)
cir4 = graphics.Circle(pt90, 5)
cir5 = graphics.Circle(pt120, 5)
cir6 = graphics.Circle(pt150, 5)
cirEnc = graphics.Circle(graphics.Point(250, 250), 100)

lineVert = graphics.Line(graphics.Point(250, 150), graphics.Point(250,350))
lineHoriz = graphics.Line(graphics.Point(150, 250), graphics.Point(350, 250))
line30 = graphics.Line(graphics.Point(250 - (100 * math.cos(math.pi/6)), (250 + 100 * (math.sin(math.pi/6)))), graphics.Point(250 + (100 * math.cos(math.pi/6)), 250 - (100 * math.sin(math.pi/6))))
line60 = graphics.Line(graphics.Point(250 - (100 * math.cos(math.pi/3)), (250 + 100 * (math.sin(math.pi/3)))), graphics.Point(250 + (100 * math.cos(math.pi/3)), 250 - (100 * math.sin(math.pi/3))))
line120 = graphics.Line(graphics.Point(250 - (100 * math.cos(math.pi/3)), (250 - 100 * (math.sin(math.pi/3)))), graphics.Point(250 + (100 * math.cos(math.pi/3)), 250 + (100 * math.sin(math.pi/3))))
line150 = graphics.Line(graphics.Point(250 - (100 * math.cos(math.pi/6)), (250 - 100 * (math.sin(math.pi/6)))), graphics.Point(250 + (100 * math.cos(math.pi/6)), 250 + (100 * math.sin(math.pi/6))))

cirEnc.draw(win)
cir.draw(win)
cir2.draw(win)
cir3.draw(win)
cir4.draw(win)
cir5.draw(win)
cir6.draw(win)

lineVert.draw(win)
lineHoriz.draw(win)
line30.draw(win)
line60.draw(win)
line120.draw(win)
line150.draw(win)

dx = 0.1
dy = -0.1
dxDiag = 0.1 * math.sqrt(2) / 2
dyDiag = 0.1 * math.sqrt(2) / 2

win.getMouse()

while True:
    if cir.getCenter().getX() >= 350:
        dx = -0.1
        dy = 0.1
        dxDiag = 0.1 * math.sqrt(2) / 2
        dyDiag = 0.1 * math.sqrt(2) / 2
    if cir.getCenter().getX() <= 150:
        dx = -dx
        dy = -dy
        dxDiag = -dxDiag
        dyDiag = -dyDiag

    cir.move(dx, 0)
    cir2.move(-dx, 0)
    cir3.move(0, dy)
    cir4.move(0, -dy)
    cir5.move(dxDiag, dyDiag)
    cir6.move(-dxDiag, dyDiag)



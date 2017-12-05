import graphics
import math

win = graphics.GraphWin("Graphics Window", 500, 500)

pt1 = graphics.Point(300, 250)
pt2 = graphics.Point(200, 250)
pt3 = graphics.Point(250, 200)
pt4 = graphics.Point(250, 300)
ptUpperLeft = graphics.Point(250 - (25 * math.sqrt(2)), 250 - (25 * math.sqrt(2)))
ptUpperRight = graphics.Point(250 + (25 * math.sqrt(2)), 250 - (25 * math.sqrt(2)))
ptLowerLeft = graphics.Point(250 - (25 * math.sqrt(2)), 250 + (25 * math.sqrt(2)))
ptLowerRight = graphics.Point(250 + (25 * math.sqrt(2)), 250 + (25 * math.sqrt(2)))

cir = graphics.Circle(pt1, 5)
cir2 = graphics.Circle(pt2, 5)
cir3 = graphics.Circle(pt3, 5)
cir4 = graphics.Circle(pt4, 5)
cir5 = graphics.Circle(ptUpperLeft, 5)
cir6 = graphics.Circle(ptUpperRight, 5)
cir7 = graphics.Circle(ptLowerLeft, 5)
cir8 = graphics.Circle(ptLowerRight, 5)
cirEnc = graphics.Circle(graphics.Point(250, 250), 50)

lineVert = graphics.Line(graphics.Point(250,200), graphics.Point(250,300))
lineHoriz = graphics.Line(graphics.Point(200, 250), graphics.Point(300, 250))
lineDownLeft = graphics.Line(graphics.Point(250 - (25 * math.sqrt(2)), 250 - (25 * math.sqrt(2))), graphics.Point(250 + (25 * math.sqrt(2)), 250 + 25 * (math.sqrt(2))))
lineUpRight = graphics.Line(graphics.Point(250 - (25 * math.sqrt(2)), 250 + (25 * math.sqrt(2))), graphics.Point(250 + (25 * math.sqrt(2)), 250 - 25 * (math.sqrt(2))))

cirEnc.draw(win)
cir.draw(win)
cir2.draw(win)
cir3.draw(win)
cir4.draw(win)
cir5.draw(win)
cir6.draw(win)
cir7.draw(win)
cir8.draw(win)
lineVert.draw(win)
lineHoriz.draw(win)
lineDownLeft.draw(win)
lineUpRight.draw(win)

dx = 0.1
dy = -0.1
dxDiag = 0.1 * math.sqrt(2) / 2
dyDiag = 0.1 * math.sqrt(2) / 2

win.getMouse()

while True:
    if cir.getCenter().getX() >= 300:
        dx = -0.1
        dy = 0.1
        dxDiag = 0.1 * math.sqrt(2) / 2
        dyDiag = 0.1 * math.sqrt(2) / 2
    if cir.getCenter().getX() <= 200:
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
    cir7.move(dxDiag, -dyDiag)
    cir8.move(-dxDiag, -dyDiag)
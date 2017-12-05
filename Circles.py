import graphics

win = graphics.GraphWin("Graphics Window", 500, 500)

def cardinalCircles():
    pt1 = graphics.Point(300, 250)
    pt2 = graphics.Point(200, 250)
    pt3 = graphics.Point(250, 200)
    pt4 = graphics.Point(250, 300)
    cir = graphics.Circle(pt1, 5)
    cir2 = graphics.Circle(pt2, 5)
    cir3 = graphics.Circle(pt3, 5)
    cir4 = graphics.Circle(pt4, 5)
    cir.draw(win)
    cir2.draw(win)
    cir3.draw(win)
    cir4.draw(win)

    dx = 0.1
    dy = -0.1

    while True:
        if cir.getCenter().getX() >= 300:
            dx = -0.1
            dy = 0.1
        if cir.getCenter().getX() <= 200:
            dx = 0.1
            dy = -0.1
        cir.move(dx, 0)
        cir2.move(-dx, 0)
        cir3.move(0, dy)
        cir4.move(0, -dy)

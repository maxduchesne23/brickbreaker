#Max Duchesne
#Project 7
#Spring 2020

#circles.py
#Uses the graphicsPlus package to create and animate circles in a window

import graphicsPlus as gr
import random
import time

def makeCircle():
    '''Makes a list of circles and animates them'''
    circle_list = []
    win = gr.GraphWin("TestWin",500,500,False)
    for i in range(50):
        circle = gr.Circle(gr.Point(random.randint(0,500),random.randint(0,500)),10)
        circle.setFill( gr.color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        circle.setOutline("red")
        circle_list.append(circle)
        circle.draw(win)
        win.update()
    for t in range(250):
        for circle in circle_list:
            circle.move(random.randint(-5, 5), random.randint(0, 8))
            win.update()
    win.getMouse()
    win.close()

if __name__ == "__main__":
    makeCircle()

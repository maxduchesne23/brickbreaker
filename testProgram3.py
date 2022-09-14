# Bruce A. Maxwell
# CS 152 Spring 2020
# Project 7 test program 3
#
# Creates a 5 x 5 grid of balls of varying sizes and colors
#

import graphicsPlus as gr
import shapes
import time

# Creates a 5x5 grid of balls where the color and sizes change over the grid
# The balls get bigger and then get smaller, testing the getRadius and setRadius functions
def main():

    # create a window
    win = gr.GraphWin( "Ball Grid", 500, 500, False )

    ball_list = []

    for i in range(5):
        for j in range(5):
            # generate the position and color
            x = (j+2) * 60
            y = (i+2) * 60
            color = gr.color_rgb( 50 + j*40, 50 + j*40, 250 - j*40 )

            # create the ball using the ball_construct function
            ball = shapes.ball_construct( (i+1)*5, [x, y], [0, 0], [0, 0], win, color )

            # draw the ball into the window using the draw function
            shapes.draw( ball )

            # add the ball to the ball_list
            ball_list.append( ball )

    txt = gr.Text( gr.Point( 250, 40 ), 'Click to continue' )
    txt.setSize( 10 )
    tsize = 10
    txt.draw( win )

    win.getMouse()
    txt.setText( 'Inhale' )

    # update the window so we can see the balls
    win.update()

    # loop for some period of time
    dt = 0.02
    for i in range(100):

        if i == 50:
            txt.setText( 'Exhale' )

        if i < 50:
            tsize += 0.5
            txt.setSize( int(tsize) )
        else:
            tsize -= 0.5
            txt.setSize( int(tsize) )
            

        # update all of the balls
        for ball in ball_list:

            # get the radius
            rad = shapes.ball_getRadius( ball )
            print(rad)

            # adjust the radius
            if i < 50:
                rad = rad + 1
            else:
                rad = rad - 1

            # set the radius
            shapes.ball_setRadius( ball, rad )

        win.update()
        time.sleep( dt*0.5 )

    txt.setSize( 16 )
    txt.setText( 'Click to continue' )
    win.update()
        
    # wait for a mouse click
    win.getMouse()

    txt.setText( 'See ya' )
    win.update()
    time.sleep(0.2)

    # close the window
    win.close()


if __name__ == "__main__":
    main()


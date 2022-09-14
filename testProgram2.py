# Bruce A. Maxwell
# CS 152 Spring 2020
# Project 7 test program 2
#
# Creates a 5 x 5 grid of balls of varying sizes and colors
# 

import graphicsPlus as gr
import shapes
import time

# Creates a 5x5 grid of balls where the color and sizes change over the grid
# The balls shift downward one at a time to test the get and setPosition functions
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

    # update the window so we can see the balls
    win.update()

    txt = gr.Text( gr.Point( 250, 50 ), 'Click to continue' )
    txt.setSize( 16 )
    txt.draw( win )

    win.getMouse()
    txt.setText( 'Shifting down' )

    dt = 0.2

    # make the balls move down one at a time with a little delay
    for ball in ball_list:
        # get the current ball position
        pos = shapes.getPosition( ball )

        txt.setText( txt.getText() + '.' )

        # move the ball down by 25 pixels
        shapes.setPosition( ball, [pos[0], pos[1] - 25] )
        win.update()
        time.sleep( dt )

    txt.setText( 'Click to continue' )
        
    # wait for a mouse click
    win.getMouse()

    txt.setText( 'See ya' )
    win.update()
    time.sleep(0.2)

    # close the window
    win.close()


if __name__ == "__main__":
    main()


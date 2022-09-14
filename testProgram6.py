# Bruce A. Maxwell
# CS 152 Project 7
# Spring 2020
# First Physics-based simulation project
#
# Test function for ball, block, and ball-block collisions

import random
import sys
import time
import graphicsPlus as gr
import shapes

# A function that creates a series of blocks
def init_blocks(x, y, size, number, win):
    bricks = []
    
    # each brick is one across and two supporting
    for i in range(number):
        b = shapes.block_construct( size, size/8,
                                   [x, i*(size/3) + y],
                                   [0, 0], [0, 0], win, gr.color_rgb( 240, 220, 190 ) )
        bricks.append( b )

    # return the list of bricks and boards
    return bricks


# Drop a ball on a set of rectangles and have them break apart
def main( argv ):

    # make a window
    win = gr.GraphWin( "Drop", 500, 500, False )

    # init the bricks and boards
    blocks = init_blocks(win.getWidth()/2, 50, 200, 5, win )

    # draw the bricks and boards into the window
    for item in blocks:
        shapes.draw( item )

    # create and draw the ball, giving it a downward acceleration
    lefttest = 135
    righttest = 365
    belowtest = 150
    demo = shapes.ball_construct( 10, [lefttest, 450], [0, 0], [0, -4], win, 'black')
    shapes.draw(demo)

    txt = gr.Text( gr.Point( 80, 250 ), 'Click to continue' )
    txt.setSize( 12 )
    txt.draw(win)

    win.getMouse()
    txt.setText( 'Testing left' )
    win.update()

    # time step 
    dt = 0.02

    # loop for 1500 time steps
    for i in range(3200):

        # update the ball falling down
        shapes.update( demo, dt )

        # keep track of which bricks don't get hit
        newblocks = []
        
        # loop over the blocks
        for block in blocks:
            # if there is a collision
            if shapes.ball_block_collision( demo, block ):
                # undraw the original block
                shapes.undraw( block )
            else:
                # if no collision, keep the brick 
                newblocks.append(block)
        # update the bricks list
        blocks = newblocks

        # check if the ball has gone out of the window
        pos = shapes.getPosition( demo )
        if pos[1] < 0 or pos[0] > 500:
            if pos[0] == lefttest:
                txt.setText('Testing bottom')
                txt.setFill( 'green')
                shapes.setVelocity( demo, [0, 0] )
                shapes.setAcceleration( demo, [4, 0] )
                shapes.setPosition(demo, [-10, belowtest] )
            elif pos[1] == belowtest:
                txt.setText('Testing right')
                txt.setFill( 'blue')
                shapes.setVelocity( demo, [0, 0] )
                shapes.setAcceleration( demo, [0, -4] )
                shapes.setPosition(demo, [righttest, 450] )
            elif pos[0] == righttest:
                txt.setText('Testing hits')
                txt.setFill( 'red')
                shapes.setVelocity( demo, [0, 0] )
                shapes.setPosition(demo, [250, 450] )

        # periodically update the window
        if i % 10 == 0:
            win.update()

    # wait for a mouse click to close
    txt.setText( 'Click to contnue' )
    txt.move( 10, 0 )
    txt.setFill( 'black' )
    win.update()
    win.getMouse()

    txt.setText( 'See ya' )
    win.update()
    time.sleep(0.2)
    win.close()


if __name__ == "__main__":
    main(sys.argv)

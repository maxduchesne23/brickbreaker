# Bruce A. Maxwell
# CS 152 Spring 2020
# Project 7 test program 5
#
# tests most of the block functions
#

import graphicsPlus as gr
import shapes
import time
import random

# Creates a platform
# Blocks fall onto the platform one at a time
# The blocks then get booted off the platform to follow a parabolic trajectory
def main():

    # create a window
    win = gr.GraphWin( "Boot the Block", 500, 500, False )

    # create a platform using a block
    platform_y = 300
    platform_dy = 20
    platform = shapes.block_construct( 150, platform_dy,
                                       [75, platform_y], [0, 0], [0, 0],
                                       win, 'black' )
    shapes.draw(platform)

    # create the boot block and draw it
    bootblock = shapes.block_construct( 50, 50,
                                        [-30, platform_y + platform_dy/2 + 25], [0, 0], [0, 0],
                                        win, 'blue' )
    shapes.draw(bootblock)

    # make some text
    txt = gr.Text( gr.Point( 350, 50 ), "Click to make something happen\nq to quit")
    txt.setSize( 12 )
    txt.draw(win)
    win.update()

    # some useful variables
    done = False
    activeblock = None
    dt = 0.02

    while not done:

        pt = win.checkMouse()
        if pt != None:

            # create a block that drop onto the platform
            activeblock_dy = 30
            activeblock = shapes.block_construct( 40, activeblock_dy,
                                                  [120, 550], [0, 0], [0, -150], win, 'red' )
            shapes.draw(activeblock)

            # loop to let the block fall down
            pos = shapes.getPosition( activeblock )
            while pos[1] > platform_y + platform_dy/2 + activeblock_dy/2:
                shapes.update( activeblock, dt )
                win.update()
                time.sleep(dt*0.5)
                pos = shapes.getPosition( activeblock )

            # set the block to the top of the platform
            shapes.setPosition( activeblock, [ pos[0], platform_y + platform_dy/2 + activeblock_dy/2 ] )

            # make the boot block accelerate
            shapes.setAcceleration(bootblock, [ 200, 0 ] )

            # loop to make the boot block move
            pos = shapes.getPosition( bootblock )
            while pos[0] < 75:
                shapes.update( bootblock, dt )
                win.update()
                time.sleep(dt*0.5)
                pos = shapes.getPosition( bootblock )

            expr = random.choice( ['Kapow!', 'Boff!', 'Boom!', 'Crash!' ] )
            txt.setText( expr )
            txt.setSize( 32 )
            txt.setFill( 'red' )
                                  

            # change the velocity and accel of the boot block
            bvel = shapes.getVelocity( bootblock )
            shapes.setAcceleration( bootblock, [0, 0] )
            shapes.setVelocity( bootblock, [-60, 0] )

            # transfer velocity to the active block
            vx = bvel[0] * (0.7 + random.random()*0.4)
            vy = 10 + random.random() * 30
            
            shapes.setVelocity( activeblock, [vx, vy] )
            shapes.setAcceleration( activeblock, [0, -200] )

            # loop to make the active block move
            pos = shapes.getPosition( activeblock )
            while pos[1] > 0:
                shapes.update( activeblock, dt )
                shapes.update( bootblock, dt )
                win.update()
                time.sleep(dt * 0.5)
                pos = shapes.getPosition( activeblock )

            # reset the boot block position and undraw the active block
            shapes.setPosition( bootblock, [-30, platform_y + platform_dy/2 + 25] )
            shapes.undraw( activeblock )

            txt.setText( "Oooh, do that again!" )
            txt.setFill( 'black' )
            txt.setSize( 16 )

        # type q to quit
        key = win.checkKey()
        if key == 'q':
            done = True

        win.update()

    # terminate
    txt.setText( 'See ya' )
    win.update()
    time.sleep(0.2)
    
    # close the window
    win.close()


if __name__ == "__main__":
    main()


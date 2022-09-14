#Max Duchesne
#Project 7
#Spring 2020

#shapes.py

import graphicsPlus as gr
import random
import time

Ipos = 0
Ivel = 1
Iacc = 2
Ishape = 3
Iwin = 4
Idrawn = 5
Isize = 6
Icolor = 7

def ball_construct(radius,pos,vel,acc,win,color = "red"):
    '''Creates a ball as a list'''
    ball = [pos,vel,acc,[],win,False,radius,color]
    lcl_pos = [pos[0],pos[1]]
    lcl_vel = [vel[0],vel[1]]
    lcl_acc = [acc[0],acc[1]]
    ball_render(ball)
    return ball

def ball_render(ball):
    '''Renders the ball from ball_construct'''
    drawn = ball[Idrawn]
    if drawn == True:
        undraw(ball)

    rad = ball[Isize]
    pos = ball[Ipos]
    win = ball[Iwin]

    circle = gr.Circle(gr.Point(pos[0],win.getHeight() - pos[1]),ball[Isize])
    circle.setFill(ball[Icolor])
    ball[Ishape] = [circle]
    if drawn == True:
        draw(ball)

def draw(object_list):
    '''Draws the object into the window'''
    if object_list[Idrawn] == False:
        for i in object_list[Ishape]:
            i.draw(object_list[Iwin])
    object_list[Idrawn] = True

def undraw(object_list):
    '''Undraws the object'''
    if object_list[Idrawn] == True:
        for i in object_list[Ishape]:
            i.undraw()
    object_list[Idrawn] = False

def getPosition( object_list ):
    '''Returns a copy of the object's position list'''
    position = object_list[Ipos][:]
    return position

def getVelocity( object_list ):
    '''Returns a copy of the object's velocity list'''
    velo = object_list[Ivel][:]
    return velo

def getAcceleration( object_list ):
    '''Returns a copy of the object's acceleration list'''
    accel = object_list[Iacc][:]
    return accel

def setVelocity( object_list, vel ):
    '''Updates the velocity information in object list with the values from vel'''
    object_list[Ivel] = vel[:]

def setAcceleration( object_list, acc ):
    '''Updates the acceleration information in object list with the values from vel'''
    object_list[Iacc] = acc[:]

def setPosition( object_list, pos ):
    '''Moves the ball to the inputted position'''
    x = object_list[Ipos][0]
    y = object_list[Ipos][1]
    object_list[Ipos] = pos[:]
    dx = pos[0] - x
    dy = pos[1] - y
    for i in object_list[Ishape]:
        i.move(dx,-dy)

def ball_getRadius( object_list ):
    '''Returns the ball's radius'''
    rad = object_list[Isize]
    return rad

def ball_setRadius( object_list, rad ):
    '''Updates the ball's radius information then calls ball_render'''
    object_list[Isize] = rad
    ball_render(object_list)

def update( object_list, dt ):
    '''Updates the position and velocity of the object list, then moves them accordingly'''
    delta_xpos = object_list[Ivel][0] * dt + 0.5 * object_list[Iacc][0] * dt * dt
    delta_ypos = object_list[Ivel][1] * dt + 0.5 * object_list[Iacc][1] * dt * dt
    object_list[Ipos][0] = object_list[Ipos][0] + delta_xpos
    object_list[Ipos][1] = object_list[Ipos][1] - delta_ypos
    delta_xvel = object_list[Iacc][0] * dt
    delta_yvel = object_list[Iacc][1] * dt
    object_list[Ivel][0] = delta_xvel + object_list[Ivel][0]
    object_list[Ivel][1] = delta_yvel + object_list[Ivel][1]
    for i in object_list[Ishape]:
        i.move(delta_xpos,-delta_ypos)

def block_construct( width, height, pos, vel, acc, win, color='blue'):
    '''Constructs a block'''
    block_list = [pos,vel,acc,[],win,False,[width,height],color]
    block_render(block_list)
    return block_list

def block_render( block_list ):
    '''Renders the block list'''
    drawn = block_list[Idrawn]
    if drawn == True:
        undraw(block_list)
        
    width = block_list[Isize][0]
    height = block_list[Isize][1]
    pos = block_list[Ipos]
    win = block_list[Iwin]

    rectangle = gr.Rectangle(gr.Point(pos[0] - .5 * width,pos[1] - .5 * height),gr.Point(pos[0] + .5 * width,pos[1] + .5 * height))
    rectangle.setFill(block_list[Icolor])
    block_list[Ishape] = [rectangle]
    if drawn == True:
        draw(block_list)

def block_getWidth( block_list ):
    '''Returns the width of the block'''
    width = block_list[Isize][0]
    return width

def block_getHeight( block_list ):
    '''Returns the height of the block'''
    height = block_list[Isize][1]
    return height

def block_setWidth( block_list, width ):
    '''Updates the width value in the block_list and calls block_render'''
    block_list[Isize][0] = width
    block_render(block_list)

def block_setHeight( block_list, height ):
    '''Updates the height value in the block_list and calls block_render'''
    block_list[Isize][1] = height
    block_render(block_list)

def ball_block_collision(ball, block):
    '''Determines if block and ball collide'''
    ballpos = getPosition(ball)
    ballxpos = ballpos[0]
    ballypos = ballpos[1]
    ballrad = ball_getRadius(ball)
    blockpos = getPosition(block)
    blockxpos = blockpos[0]
    blockypos = blockpos[1]
    blockwidth = block_getWidth(block)
    blockheight = block_getHeight(block)
    collide = False
    if abs(ballxpos - blockxpos) <= abs(ballrad + blockwidth * 0.5) and abs(ballypos - blockypos) <= abs(ballrad + blockheight * 0.5):
        collide = True
    else:
        collide = False
    return collide
        

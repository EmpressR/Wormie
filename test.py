import keyboard
import time
from graphics import *
from random import choice

# --------------------------------------------------------------------------------------------------

width = 500
height = 500

key = ""

# --------------------------------------------------------------------------------------------------


def movement(key):

    if keyboard.is_pressed("Right"):
        key = "d"

    elif keyboard.is_pressed("Left"):
        key = "a"

    elif keyboard.is_pressed("Down"):
        key = "s"

    elif keyboard.is_pressed("Up"):
        key = "w"

    return key

# ---------------------------------------------------


def horizontal_movement(x):

    global key

    key = movement(key)

    if key == "d":
        x += 20

    elif key == "a":
        x -= 20

    return x


def vertical_movement(y):

    global key

    key = movement(key)

    if key == "s":
        y += 20

    elif key == "w":
        y -= 20

    return y

# --------------------------------------------------------------------------------------------------


def main():

    x = 0
    y = 0

    win = GraphWin("Wormie", width, height)
    win.setBackground(color_rgb(00, 55, 00))

    radius = 10

    worm = Rectangle(Point((width / 2) - radius + x, (height / 2) - radius + y),
                     Point((width / 2) + radius + x, (height / 2) + radius + y))

    while True:

        worm.undraw()
        worm = Rectangle(Point((width / 2) - radius + x, (height / 2) - radius + y),
                         Point((width / 2) + radius + x, (height / 2) + radius + y))
        worm.setFill("red")
        worm.setWidth(5)
        worm.draw(win)

        x = horizontal_movement(x)
        y = vertical_movement(y)

        update(10)


main()


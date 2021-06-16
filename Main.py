import keyboard
import time
from graphics import *
import random

# --------------------------------------------------------------------------------------------------

width = 500
height = 500

key = ""

win = GraphWin("Wormie", width, height)
win.setBackground(color_rgb(00, 55, 00))


# --------------------------------------------------------------------------------------------------


def movement(key):

    if keyboard.is_pressed("Left"):
        key = "a"

    elif keyboard.is_pressed("Right"):
        key = "d"

    elif keyboard.is_pressed("Up"):
        key = "w"

    elif keyboard.is_pressed("Down"):
        key = "s"

    return key

# ---------------------------------------------------


def horizontal_movement(x):

    global key

    key = movement(key)

    if key == "a":
        x -= 20

    elif key == "d":
        x += 20

    return x


def vertical_movement(y):

    global key

    key = movement(key)

    if key == "w":
        y -= 20

    elif key == "s":
        y += 20

    return y

# --------------------------------------------------------------------------------------------------


def main():

    while True:

        global key
        points = 0
        body_parts = 1
        food_count = 1

        game = True

        x = 0
        y = 0

        radius = 10

        worm_head = Rectangle(Point((width / 2) - radius + x, (height / 2) - radius + y),
                              Point((width / 2) + radius + x, (height / 2) + radius + y))

        worm = [worm_head]

        food = make_food(worm)

        while game:

            worm_head.undraw()
            worm_head = Rectangle(Point((width / 2) - radius + x, (height / 2) - radius + y),
                                  Point((width / 2) + radius + x, (height / 2) + radius + y))

            worm_body = Rectangle(Point((width / 2) - radius + x, (height / 2) - radius + y),
                                  Point((width / 2) + radius + x, (height / 2) + radius + y))

            if points == body_parts:

                worm.append(worm_body)
                body_parts += 1

                food.undraw()
                food = make_food(worm)
                food_count = 1

            # worm.xy = worm.getCenter()
            # print(worm.xy)

            worm_head.setFill("red")
            worm_head.setWidth(0)
            worm_head.draw(win)

            food.setFill("black")
            food.setWidth(0)

            if food_count == 1:
                food.draw(win)
                food_count = 0

            x = horizontal_movement(x)
            y = vertical_movement(y)

            game = game_over(worm_head.p1.x, worm_head.p1.y, worm_head.p2.x, worm_head.p2.y)
            print(game)

            points = eating(food.p1.x, food.p1.y, worm_head, points)

            if not game:
                print("Game Over2!")
                worm_head.undraw()
                food.undraw()
                key = ""

            # win.close()

            update(10)

# ---------------------------------------------------


def game_over(p1x, p1y, p2x, p2y):

    if p1x == 0:
        return False

    if p1y == 0:
        return False

    if p2x == 500:
        return False

    if p2y == 500:
        return False

    return True

# --------------------------------------------------------------------------------------------------


def make_food(worm):

    f1x = random.randint(10, 490)
    f1y = random.randint(10, 490)

    for piece in worm:

        if piece.p1.x <= f1x <= piece.p2.x:
            if piece.p2.y <= f1y + 15 <= piece.p2.y:

                f1x = random.randint(10, 490)

    f2x = f1x + 15
    f2y = f1y + 15

    return Rectangle(Point(f1x, f1y), Point(f2x, f2y))

# --------------------------------------------------------------------------------------------------


def eating(f1x, f1y, worm_head, points):

    if worm_head.p1.x <= f1x <= worm_head.p2.x:
        if worm_head.p2.y <= f1y + 15 <= worm_head.p2.y:
            points += 1
            return points


main()


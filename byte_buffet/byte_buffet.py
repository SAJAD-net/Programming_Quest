#!/usr/bin/env python3

import curses
import random
import time

# initialize the screen.
scr = curses.initscr()
curses.noecho()
curses.cbreak()
scr.keypad(True)
curses.curs_set(False)
scr.nodelay(True)

MAXL = curses.LINES - 1
MAXC = curses.COLS - 1

# settings.
PLAYNIG = True
world = []

PLAYER_L = PLAYER_C = 0
PLAYER_SYM = "^"

food = []
FOOD_NUM = 10
FOOD_AGE = 300
FOOD_SYM = "*"

SCORE = 10

enemy = []
ENEMY_NUM = 5
ENEMY_SYM = "E"


TESTING = False


def random_place():
    """ generates a random x and y between 0 and MAXL, 0 and MAXC. """

    a = random.randint(0, MAXL - 1)
    b = random.randint(0, MAXC - 1)
    while world[a][b] != " ":
        a = random.randint(0, MAXL - 1)
        b = random.randint(0, MAXC - 1)

    return (a, b)


def init():
    """ initialize the space, player, foods and enemies. """

    global PLAYER_L, PLAYER_C

    # initialize the space.
    for i in range(MAXL+1):
        world.append([])
        for _ in range(MAXC+1):
            world[i].append(" " if random.random() > 0.03 else ".")

    # initialize the player.
    PLAYER_L, PLAYER_C = random_place()

    # initialize foods.
    for i in range(FOOD_NUM):
        fl, fc = random_place()
        fa = random.randint(FOOD_AGE, FOOD_AGE)
        food.append((fl, fc, fa))

    # initialize enemies.
    for i in range(ENEMY_NUM):
        el, ec = random_place()
        enemy.append((el, ec))


def draw():
    """  draw the space, player (spaceship), foods and enemies. """

    for i in range(MAXL):
        for j in range(MAXC):
            scr.addch(i, j, world[i][j])

    # print the SCORE.
    scr.addstr(1, 1, f"Score : {SCORE}", curses.A_BOLD)

    # draw the foods.
    for fl, fc, _ in food:
        scr.addch(fl, fc, FOOD_SYM)

    # draw the enemies.
    for el, ec in enemy:
        scr.addch(el, ec, ENEMY_SYM)

    # draw the player (spaceship).
    scr.addch(PLAYER_L, PLAYER_C, PLAYER_SYM, curses.A_BOLD)
    scr.refresh()


def in_range(a, mn, mx):
    """ checks if 'a' is between mn and mx. """

    if a > mx:
        a = mx
    elif a < mn:
        a = mn
    return a


def move(c):
    """ move the spaceship base on 'awsd'. """

    global PLAYER_L, PLAYER_C

    if c == "w" and world[PLAYER_L - 1][PLAYER_C] != ".":
        PLAYER_L -= 1
    elif c == "s" and world[PLAYER_L + 1][PLAYER_C] != ".":
        PLAYER_L += 1
    elif c == "a" and world[PLAYER_L][PLAYER_C - 1] != ".":
        PLAYER_C -= 1
    elif c == "d" and world[PLAYER_L][PLAYER_C + 1] != ".":
        PLAYER_C += 1

    PLAYER_L = in_range(PLAYER_L, 0, MAXL-1)
    PLAYER_C = in_range(PLAYER_C, 0, MAXC-1)


def check_food():
    """ checks the foods' status. """

    global SCORE

    # check if any food has been eaten.
    # replace it with a new food.
    for i in range(len(food)):
        fl, fc, fa = food[i]
        fa -= 1
        if fl == PLAYER_L and fc == PLAYER_C:
            SCORE += 10
            fa = random.randint(FOOD_AGE, FOOD_AGE)
            fl, fc = random_place()

        # regenerate the food when its age (fa) reaches 0.
        if fa <= 0:
            fa = random.randint(FOOD_AGE, FOOD_AGE)
            fl, fc = random_place()

        food[i] = (fl, fc, fa)


def enemy_move():
    """ move the enemies. """

    global PLAYNIG

    for i in range(len(enemy)):
        el, ec = enemy[i]

        # end the game if spaceship hits the enemies.
        if PLAYER_L == el and PLAYER_C == ec and not TESTING:
            PLAYNIG = False
            scr.addstr(MAXL//2, MAXC//2, "YOU DIED !", curses.A_BOLD)
            scr.refresh()
            curses.napms(1000)

        # move the enemies toward the spaceship.
        if random.random() > 0.9:
            if el > PLAYER_L:
                el -= 1
        if random.random() > 0.9:
            if el < PLAYER_L:
                el += 1
        if random.random() > 0.9:
            if ec > PLAYER_C:
                ec -= 1
        if random.random() > 0.9:
            if ec < PLAYER_C:
                ec += 1

        el = in_range(el, 0, MAXL - 1)
        ec = in_range(ec, 0, MAXC - 1)
        enemy[i] = (el, ec)


def main():
    """ the main function. """

    global PLAYNIG

    # initialize the game.
    init()

    # the main loop of the game.
    while PLAYNIG:
        try:
            # try to get keys from keyboard
            c = scr.getkey()
        except:
            c = " "

        # move the spaceship based on 'wasd'.
        if c in "wasd":
            move(c)

        # end the game if 'q' was hit.
        elif c == "q":
            PLAYNIG = False

        # check if any food has been eaten.
        check_food()

        # move the enemies
        enemy_move()

        # draw the game
        draw()

        time.sleep(0.05)

    # print `Thanks for PLAYNIG` in the middle of the window.
    scr.addstr(MAXL//2, MAXC//2, "Thanks for PLAYNIG!", curses.A_BOLD)
    scr.refresh()
    # wait for a second
    curses.napms(1000)
    scr.clear()
    scr.refresh()
    curses.curs_set(True)

main()

#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# Makes a sprite move on circuit python

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("ball.bmp")
# a list of sprites that will be updated every frame
sprites = []


def main():
    # this function sets the background

    background = stage.Grid(image_bank_1, 10, 8)

    ball_one = stage.Sprite(image_bank_1, 3, 64, 56)
    sprites.append(ball_one)
    ball_two = stage.Sprite(image_bank_1, 2, 75, 56)
    sprites.insert(0, ball_two)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = sprites + [background]
    game.render_block()

    while True:
        # get user inputs
        keys = ugame.buttons.get_pressed()
        # print(keys)

        if keys & ugame.K_UP:
            ball_one.move(ball_one.x, ball_one.y - 2)
            pass
        if keys & ugame.K_DOWN:
            ball_one.move(ball_one.x, ball_one.y + 2)
            pass
        if keys & ugame.K_LEFT:
            ball_one.move(ball_one.x - 2, ball_one.y)
            pass
        if keys & ugame.K_RIGHT:
            ball_one.move(ball_one.x + 2, ball_one.y)
            pass
        # update game logic

        game.render_sprites(sprites)
        game.tick()


if __name__ == "__main__":
    main()

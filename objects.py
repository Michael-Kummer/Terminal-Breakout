"""
Objects.py plugs into breakout.py

Block:
    - Create a map in dictionary for each block + status
    - Map is actively edited by breakout.check_collision during runtime
    - Draw blocks

Paddle:
    - Moves paddle left and right.
    - Defaults to the bottom of the screen

Ball:
    - Moves ball in all 4 directions
    - breakout.check_collision changes xvelocity and yvelocity during runtime
    - Draws ball
"""

import curses

class Block:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.max_height, self.max_width = self.stdscr.getmaxyx()
        self.map = {}
        self.block_width = 4
        self.block_height = 1  # Define the height of a block
        self.spawn_map()

    def spawn_map(self):
        blockxcount = self.max_width // (self.block_width + 2)
        blockycount = 4

        for j in range(blockycount):
            for i in range(blockxcount):
                blocknumber = (j * (i - 1)) + i
                self.map[blocknumber] = 1  # Use 1 to mark active blocks

    def draw(self, x, y, block_width):
        """
        Draws line by line. checks if block is active
        Inputs: block x pointer, block y pointer, block width
        """
        for blocknumber in self.map.keys():
            if self.map[blocknumber] == 1:  # Check if block is active
                for j in range(block_width):
                    if 0 <= y < self.max_height and 0 <= x + j < self.max_width:
                        try:
                            self.stdscr.addch(y, x + j, "█")
                        except curses.error:
                            pass
class Paddle:
    def __init__(self, x, y, width, stdscr):
        self.x = x
        self.y = y
        self.width = width
        self.map = [0] * self.width
        self.max_height, self.max_width = stdscr.getmaxyx()

    def draw(self, stdscr):
        for i in range(self.width):
            if self.x + i < self.max_width:
                stdscr.addch(self.y, self.x + i, curses.ACS_CKBOARD)

    def move_left(self):
        if self.x > 3:
            self.x -= 3

    def move_right(self):
        if self.x + self.width < self.max_width:
            self.x += 3


class Ball:
    def __init__(self, x, y, velocity, stdscr):
        self.x = x
        self.y = y
        self.velocity = velocity

        # ball velocities
        self.xvelocity = 1
        self.yvelocity = -1

        self.max_height, self.max_width = stdscr.getmaxyx()

    def draw(self, stdscr):
        stdscr.addch(self.y, self.x, ord("o"))

    def move_up(self):
        if self.y != 0:
            self.y -= 1

    def move_down(self):
        if self.y < self.max_height - 1:
            self.y += 1

    def move_left(self):
        if self.x != 0:
            self.x -= 1

    def move_right(self):
        if self.x <= self.max_width:
            self.x += 1

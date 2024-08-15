import curses


class Block:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def draw(self, x, y, block_width):
        max_height, max_width = self.stdscr.getmaxyx()
        for i in range(2):
            for j in range(block_width):
                if 0 <= y + (i - 1) < max_height and 0 <= x + j < max_width:
                    try:
                        self.stdscr.addch(y + (i - 1), x + j, curses.ACS_BLOCK)
                    except curses.error:
                        pass


class Paddle:
    def __init__(self, x, y, width, stdscr):
        self.x = x
        self.y = y
        self.width = width
        self.max_height, self.max_width = stdscr.getmaxyx()

    def draw(self, stdscr):
        for i in range(self.width):
            if self.x + i < self.max_width:
                stdscr.addch(self.y, self.x + i, curses.ACS_CKBOARD)

    def move_left(self):
        if self.x > 0:
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

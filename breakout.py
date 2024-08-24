# ----------------------------------------------------
#
#  /_  __/__  _________ ___  (_)___  ____ _/ /  / __ )________  ____ _/ /______  __  __/ /_
#   / / / _ \/ ___/ __ `__ \/ / __ \/ __ `/ /  / __  / ___/ _ \/ __ `/ //_/ __ \/ / / / __/
#  / / /  __/ /  / / / / / / / / / / /_/ / /  / /_/ / /  /  __/ /_/ / ,< / /_/ / /_/ / /_
# /_/  \___/_/  /_/ /_/ /_/_/_/ /_/\__,_/_/  /_____/_/   \___/\__,_/_/|_|\____/\__,_/\__/
#
# Author: Michael
# ----------------------------------------------------

import curses
import time
from objects import *

class Breakout:
    def __init__(self, stdscr):
        curses.noecho()
        self.stdscr = stdscr
        curses.curs_set(0)
        self.max_height, self.max_width = stdscr.getmaxyx()
        self.paddle_size = 20
        self.paddle = Paddle(self.max_width // 2, self.max_height - 2, self.paddle_size, stdscr)
        self.ball = Ball(self.max_width // 3, self.max_height // 2, 0, stdscr)
        self.block = Block(stdscr)   
        self.block_width = 10
        self.current_time = time.time()


    def draw_paddle(self):
        """
        Spawns paddle
        Inputs: None
        Returns: None
        """
        self.paddle.draw(self.stdscr)

    def draw_ball(self):
        """
        TODO: create a self.xvelocity and self.yvelocity.
            Spawns going 45* down to paddle in the middle
        Spawns ball
        Inputs: None
        Returns: None
        """
        if self.ball.yvelocity > 0:
            self.ball.move_up()
        elif self.ball.yvelocity < 0:
            self.ball.move_down()

        if self.ball.xvelocity > 0:
            self.ball.move_right()
        elif self.ball.xvelocity < 0:
            self.ball.move_left()

        self.ball.draw(self.stdscr)

    def draw_blocks(self):
        """
        Spawns blocks - this is called recursively
        Inputs: None
        Returns: None
        """

        block_height = 2  # Assuming each block's visual height is set as 2 for spacing
        blockxcount = self.max_width // (self.block.block_width + 2)

        for blocknumber, block_info in self.block.map.items():
            if block_info[0] == 1:  # Check if the block is active
                x = (blocknumber % blockxcount) * (self.block.block_width + 2)
                y = (blocknumber // blockxcount) * block_height
                self.block.draw(x, y, self.block.block_width)


    def check_collision(self):
        """
        Checks collision between ball, paddle, block
        Inputs: None
        Returns: None
        """
        # Screen Side Collision
        if self.ball.x == 0 or self.ball.x == self.max_width - 2:
            self.ball.xvelocity *= -1
        if self.ball.y == 0 or self.ball.y == self.max_height - 1:
            self.ball.yvelocity *= -1

        # Block Collision
        self.block_collision()

        # Paddle Collision
        self.map = [self.paddle.x + i for i in range(self.paddle.width)]
        if self.ball.y == self.paddle.y - 1:
            for pos in self.map:
                if self.ball.x == pos:
                    self.ball.yvelocity *= -1
                    break

    def block_collision (self):
        """
        [key] = {value_list}
        [block #] = {[active_state,ycoord,xcoord1,xcoord2,xcoord3,xcoord4]}
        This is mapped out for every block
        """
       
        blockxcount = self.max_width // (self.block.block_width + 2)
        block_width = self.block.block_width
        block_height = 2  # Adjusted to match `spawn_map` settings

        for blocknumber, status in self.block.map.items():
            if status[0] == 1:  # Check active state
                block_x = (blocknumber % blockxcount) * (block_width + 2)
                block_y = (blocknumber // blockxcount) * block_height

                if block_x <= self.ball.x <= block_x + block_width and \
                   block_y <= self.ball.y <= block_y + block_height:
                    self.block.map[blocknumber][0] = 0  # Deactivate block
                    self.ball.yvelocity *= -1
                    break

    def run(self):
        """
        Coordinates the game logic
        Inputs: None
        Returns: None
        """
        self.stdscr.nodelay(True)

        while True:
            key = self.stdscr.getch()

            # Paddle Movement
            if key == curses.KEY_LEFT or key == ord("h"):
                self.paddle.move_left()
            elif key == curses.KEY_RIGHT or key == ord("l"):
                self.paddle.move_right()
            elif key == ord("q"):
                break

            # Time-based Game Logic
            if time.time() - self.current_time > 1 / 20:
                self.stdscr.clear()  # Clear the screen once
                self.check_collision()  # Handle ball collisions

                # Redraw game components
                self.draw_paddle()
                self.draw_ball()
                self.draw_blocks()

                self.stdscr.refresh()  # Refresh the screen after all draws

                # Reset the timer
                self.current_time = time.time()


def main(stdscr):
    breakout = Breakout(stdscr)
    breakout.run()


if __name__ == "__main__":
    curses.wrapper(main)

# ----------------------------------------------------
# Breakout Game
#
# Author: Michael
# ----------------------------------------------------
import curses
import time
from objects import *


class Breakout:
    def __init__(self, stdscr):
        """
        Initalizes an empty screen
        Inputs: None
        Returns: None
        """
        # Curses init stuff
        curses.noecho()
        self.stdscr = stdscr
        curses.curs_set(0)
        # Setting heights and sizes
        self.max_height, self.max_width = stdscr.getmaxyx()
        self.paddle_size = 20
        self.paddle = Paddle(
            self.max_width // 2, self.max_height - 2, self.paddle_size, stdscr
        )
        self.ball = Ball(self.max_width // 3, self.max_height // 2, 0, stdscr)
        self.block = Block(stdscr)
        self.block_width = 10

        # initalizing block grid
        self.grid_width = self.max_width // self.block_width
        self.grid_height = 4
        self.grid = [
            [0 for _ in range(self.grid_width)] for _ in range(self.grid_height)
        ]
        
        #Initalize time variable
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
        TODO: create a self.xvelocity and self.yvelocity. Spawns going 45* down to paddle in the middle
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
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                x = j * (self.block_width + 2)
                y = i * 4
                self.block.draw(x, y, self.block_width)



    def check_collision(self):
        """
        Checks collision between ball, paddle, brick
        Inputs: None
        Returns: None
        """
        # Screen Side Collision
        if self.ball.x == 0 or self.ball.x == self.max_width - 2:
            self.ball.xvelocity *= -1
        if self.ball.y == 0 or self.ball.y == self.max_height - 1:
            self.ball.yvelocity *= -1

        # Paddle Collision
        if self.ball.y == self.paddle.y - 1:
            for i in range(self.paddle_size):
                if (
                    self.ball.x <= self.paddle.x + i
                    and self.ball.y == self.paddle.y + 1
                ):
                    self.ball.yvelocity *= -1

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
            if time.time() - self.current_time > 1/30:
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

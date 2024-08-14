#----------------------------------------------------
# Breakout Game
#
# Author: Michael
#----------------------------------------------------
import curses

class Breakout:
    def __init__(self, stdscr):
        '''
        Initalizes an empty screen
        Inputs: None
        Returns: None
        '''
        curses.noecho()
        self.stdscr = stdscr
        curses.curs_set(0)
        self.max_height, self.max_width = stdscr.getmaxyx()
        self.paddle = Paddle(self.max_width//2, self.max_height - 2, 10 ,stdscr)
        self.ball = Ball(self.max_width // 2, self.max_height // 2, stdscr)
        self.block = Block(stdscr)

        self.grid_width = self.max_width // 5
        self.grid_height = 4
        self.grid = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]

    def draw_paddle(self):
        '''
        Spawns paddle
        Inputs: None
        Returns: None
        '''
        self.paddle.draw(self.stdscr)

    def draw_ball(self):
        '''
        Spawns ball
        Inputs: None
        Returns: None
        '''
        self.ball.draw(self.stdscr)    

    def draw_blocks(self):
        '''
        Spawns blocks - this is called recursively
        Inputs: None
        Returns: None
        '''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                x = j * 5
                y = i * 2
                self.block.draw(x,y,)    
                    
    def check_collision(self):
        '''
        Checks collision between ball, paddle, brick
        Inputs: None
        Returns: ball->paddle, ball->brick, ball->screensides
        '''  
        pass

    def run(self):
        '''
        Coordinates the game logic
        Inputs: None
        Returns: None   
        '''        
        self.draw_paddle()
        self.draw_ball()
        self.draw_blocks()

        self.stdscr.refresh()

        while True:
            key = self.stdscr.getch()

            if key == curses.KEY_LEFT or key == ord('h'):
                self.paddle.move_left()
            elif key ==curses.KEY_RIGHT or key == ord("l"):
                self.paddle.move_right()
            elif key == ord('q'):
                break
            
            self.draw_blocks()
            self.stdscr.clear()
            self.draw_paddle()
            self.draw_ball()
            self.draw_blocks()
            self.stdscr.refresh()

class Block:
    def __init__(self,stdscr):
        self.stdscr = stdscr

    def draw(self,x,y):
        for i in range(3):
            self.stdscr.addch(y, x + i, curses.ACS_BLOCK)
        self.stdscr.addstr(y, x + 4, ' ')


class Paddle:
    def __init__(self,x,y,width,stdscr):
        self.x = x
        self.y = y
        self.width = width
        self.max_height, self.max_width = stdscr.getmaxyx()

    def draw(self,stdscr):
        for i in range(self.width):
            stdscr.addch(self.y,self.x+i,curses.ACS_CKBOARD)

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self):
        if self.x + self.width < self.max_width:
            self.x +=1

class Ball:
    def __init__(self,x,y,stdscr):
        self.x = x
        self.y = y
        self.max_height, self.max_width = stdscr.getmaxyx()

    def draw(self,stdscr):
        stdscr.addch(self.y,self.x, ord('o'))

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
        if self.x != self.max_width:
            self.x += 1


def main(stdscr):
    breakout = Breakout(stdscr)
    breakout.run()

if __name__ == "__main__":
    curses.wrapper(main) 

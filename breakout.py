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
        #Curses init stuff
        curses.noecho()
        self.stdscr = stdscr
        curses.curs_set(0)
        #Setting heights and sizes
        self.max_height, self.max_width = stdscr.getmaxyx()
        self.paddle_size = 20
        self.paddle = Paddle(self.max_width//2, self.max_height - 2, self.paddle_size ,stdscr)
        self.ball = Ball(self.max_width // 3, self.max_height // 2,0, stdscr)
        self.block = Block(stdscr)
        self.block_width = 10

        #initalizing block grid
        self.grid_width = self.max_width // self.block_width
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
        TODO: create a self.xvelocity and self.yvelocity. Spawns going 45* down to paddle in the middle
        Spawns ball
        Inputs: None
        Returns: None
        '''
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
        '''
        Spawns blocks - this is called recursively
        Inputs: None
        Returns: None
        '''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                x = j * (self.block_width+2)
                y = i * 4
                self.block.draw(x,y,self.block_width)    
                    
    def check_collision(self):
        '''
        Checks collision between ball, paddle, brick
        Inputs: None
        Returns: None
        '''  
        if self.ball.x == 0 or self.ball.x == self.max_width-2:
            self.ball.xvelocity *= -1
        if self.ball.y == 0 or self.ball.y == self.max_height-1:
            self.ball.yvelocity *= -1

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
           
            self.check_collision()
            self.draw_blocks()
            self.stdscr.clear()
            self.draw_paddle()
            self.draw_ball()
            self.draw_blocks()
            self.stdscr.refresh()

class Block:
    def __init__(self,stdscr):
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
    def __init__(self,x,y,width,stdscr):
        self.x = x
        self.y = y
        self.width = width
        self.max_height, self.max_width = stdscr.getmaxyx()

    def draw(self,stdscr):
        for i in range(self.width):
            if self.x + i < self.max_width:
                stdscr.addch(self.y,self.x+i,curses.ACS_CKBOARD)

    def move_left(self):
        if self.x > 0:
            self.x -= 3

    def move_right(self):
        if self.x + self.width < self.max_width:
            self.x += 3

class Ball:
    def __init__(self,x,y,velocity,stdscr):
        self.x = x
        self.y = y
        self.velocity = velocity
       
       #ball velocities
        self.xvelocity = 1
        self.yvelocity = -1

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
        if self.x <= self.max_width:
            self.x += 1

def main(stdscr):
    breakout = Breakout(stdscr)
    breakout.run()

if __name__ == "__main__":
    curses.wrapper(main) 

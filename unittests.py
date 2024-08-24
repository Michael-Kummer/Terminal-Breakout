import objects 
import curses

def main(stdscr):
    stdscr.clear()

    block = objects.Block(stdscr)

    for i in block.map:
        print("key={}, value = {}".format(i, block.map[i]))
        stdscr.addstr(i,0, "key = {i}")
        stdscr.refresh()
    
    

    while True:
        key = stdscr.getch()
        
        if key == ord('q'):
            break

    stdscr.clear()

if __name__ == '__main__':
    curses.wrapper(main)


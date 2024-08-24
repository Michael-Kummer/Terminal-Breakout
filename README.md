# Terminal-Breakout

If your terminal has Python, you can play Breakout entirely in it.

## Current Features
- Draws the blocks, ball, and paddle.
- Can hit blocks and they disappear

## TODO List
- ✔️ Create a velocity system for the ball.
- ✔️ Implement a collision system between the ball and screen sides.
- ❌ Implement a collision system between the ball and blocks (currently, it feels unnatural and does not flag active status correctly).
- ❌ Implement a loss system - default the loss to shutting down the game for now.
- ❌ Implement "sides" of the paddle to change the angle of the ball's rebound.
- ❌ Implement a power-up system.
- ❌ Ensure that any unexpected exits do not leave the curses library in an awkward state, causing the user to have to "reset" their terminal.
- ❌ Implement color for the ball and blocks.


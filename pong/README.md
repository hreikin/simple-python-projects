# Pong
This is a very basic version of Pong which uses the Kivy framework for the GUI. Currently the players can score points and the ball bounces of the top and bottom sides as well as the players paddles, when it bounces of the paddles the speed of the ball increases slightly. There is no menu or score limit at present.

## Possible Next Steps
- Add some nicer graphics / images. (Hint: check out the source property on the graphics instructions like circle or Rectangle, to set an image as the texture.)
- Make the game end after a certain score. Maybe once a player has 10 points, you can display a large “PLAYER 1 WINS” label.
- Add a main menu to start, pause and reset the game. (Hint: check out the Button and Label classes, and figure out how to use their add_widget and remove_widget functions to add or remove widgets dynamically.
- Make it a 4 player Pong Game. Most tablets have Multi-Touch support, so wouldn’t it be cool to have a player on each side and have four people play at the same time?
- Fix the simplistic collision check so hitting the ball with an end of the paddle results in a more realistic bounce.
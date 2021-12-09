# Import modules required to create a basic Kivy based pong app.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

# The "PongPaddle" widget holds the score for the player(s) and implements 
# a "ball_bounce" method so the ball bounces differently based on where it 
# hits the racket and speeds it up slightly each time it is hit.
class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

# The "PongBall" class sets the velocity of the ball and animates the 
# movement of the ball.
class PongBall(Widget):
    # The velocity of the ball on the x and y axis.
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # Creates a "ReferenceListProperty" so we can use "ball.velocity" as a 
    # shorthand when calling it.
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # The "move" function will move the ball one step. This will be called 
    # in equal intervals to animate the ball when it is moving.
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

# Create a "widget" class.
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    # Sets a random x and y velocity for the ball and resets its position.
    def serve_ball(self, vel = (4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # Allows the ball to bounce of the player paddles.
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # Allows the ball to bounce off the top and bottom of the screen.
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # Allows the ball to go off the sides of the screen to score points.
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    # Implements the "on_touch_move" method so when a player presses down on 
    # either side of the screen the paddles will move.
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

# Return the PongGame widget as the root element for the applications UI. 
# Calls the "serve_ball" function to serve the ball and uses the "Clock" 
# module to create the interval ("schedule_interval") at which the ball is 
# updated.
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

# Start the Kivy application.
if __name__ == "__main__":
    PongApp().run()
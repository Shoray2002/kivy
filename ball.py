from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Ellipse, Color, Line
from kivy.clock import Clock
from kivy.metrics import dp
import random


Builder.load_file('./style.kv')


class Ball(Widget):
    # def __init__(self, **kwargs) -> None:
    #     super().__init__(**kwargs)
    #     self.ball_size = dp(150)
    #     self.vx = 5
    #     self.vy = 5
    #     with self.canvas:
    #         Color(0,0,255)
    #         self.ball = Ellipse(pos=self.center, size=(
    #             self.ball_size, self.ball_size))
    #     Clock.schedule_interval(self.update, 1/120)

#    change color of ball on collision

    def update(self, *args):
        x, y = self.ball.pos
        x += self.vx
        y += self.vy
        if x < 0:
            self.vx = -self.vx
            x = 0
        elif x > self.width-self.ball_size:
            self.vx = -self.vx
            x = self.width-self.ball_size

        if y < 0:
            self.vy = -self.vy
            y = 0
        elif y > self.height-self.ball_size:
            self.vy = -self.vy
            y = self.height-self.ball_size

        self.ball.pos = (x, y)


class BallApp(App):
    def build(self):
        return Ball()


BallApp().run()

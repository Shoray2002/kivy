
from kivy.app import App

def on_touch_down(self, touch):
    if touch.x > self.width/2:
        self.CURRENT_SPEED_X = -self.SPEED_X
    else:
        self.CURRENT_SPEED_X = +self.SPEED_X

def on_touch_up(self, touch):
    self.CURRENT_SPEED_X = 0

def on_key_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.CURRENT_SPEED_X = self.SPEED_X
    elif keycode[1] == 'right':
        self.CURRENT_SPEED_X = -self.SPEED_X
    elif keycode[1] == 'escape':
        App.get_running_app().stop()

def on_key_up(self, keyboard, keycode):
    if keycode[1] == 'left' or keycode[1] == 'right':
        self.CURRENT_SPEED_X = 0

def keyboard_closed(self):
    self.keyboard.unbind(on_key_down=self.on_key_down)
    self.keyboard.unbind(on_key_up=self.on_key_up)

    self.keyboard = None

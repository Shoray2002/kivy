
from kivy.properties import Clock
from kivy.graphics import SmoothLine
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.app import App
from os import times
from kivy import platform
from kivy.core.window import Window
# from kivy.config import Config
# Config.set('graphics', 'width', '900')
# Config.set('graphics', 'height', '400')
Window.size = (900, 400)


class MainWidget(Widget):
    from transform import transform_2D, tranform_perspective
    from user_input import on_key_down, on_key_up, keyboard_closed, on_touch_down, on_touch_up

    persepective_point_x = NumericProperty(0)
    persepective_point_y = NumericProperty(0)
    V_NB_LINES = 14
    V_LINES_SPACING = 0.25
    vertical_lines = []

    H_NB_LINES = 10
    H_LINES_SPACING = .1
    horizontal_lines = []

    SPEED_X = 20
    SPEED_Y = 2
    CURRENT_SPEED_X = 0
    current_offset_y = 0
    current_offset_x = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vert_lines()
        self.init_horizontal_lines()
        if platform in ['win', 'linux', 'macosx']:
            print("Platform: "+platform)
            self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self.keyboard.bind(on_key_down=self.on_key_down)
            self.keyboard.bind(on_key_up=self.on_key_up)
        Clock.schedule_interval(self.update, 1/60)

    def init_vert_lines(self):
        with self.canvas:
            # points=[self.width, 0, self.width, self.height], width=2)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(SmoothLine(width=1.1))

    def init_horizontal_lines(self):
        with self.canvas:
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(SmoothLine())

    def get_line_x_from_index(self, index):
        central_line_x = int(self.persepective_point_x)
        spacing = int(self.width * self.V_LINES_SPACING)
        central_line_x += spacing/2
        offset = index-0.5
        return int(central_line_x + spacing * offset+self.current_offset_x)

    def update_vert_lines(self):
        central_line_x = int(self.width / 2)
        spacing = int(self.width * self.V_LINES_SPACING)
        central_line_x += spacing/2
        offset = -int(self.V_NB_LINES/2)
        for i in range(0, self.V_NB_LINES):
            line_x = int(central_line_x + (spacing) *
                         offset+self.current_offset_x)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def update_horizontal_lines(self):
        central_line_x = int(self.width / 2)
        spacing = self.V_LINES_SPACING * self.width
        offset = int(self.V_NB_LINES / 2) - 0.5

        xmin = central_line_x-offset*spacing+self.current_offset_x
        xmax = central_line_x+offset*spacing+self.current_offset_x
        spacing_y = self.H_LINES_SPACING*self.height

        for i in range(0, self.H_NB_LINES):
            line_y = int(i*spacing_y-self.current_offset_y)
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def update(self, dt):
        self.update_vert_lines()
        self.update_horizontal_lines()
        time_factor = dt*60
        spacing_y = self.H_LINES_SPACING*self.height
        spacing_x = self.V_LINES_SPACING*self.width
        self.current_offset_y += self.SPEED_Y*time_factor
        if self.current_offset_y > spacing_y:
            self.current_offset_y -= spacing_y
        if self.current_offset_x > self.width+2*spacing_x:
            self.current_offset_x = self.width+2*spacing_x
        if self.current_offset_x < -(self.width+2*spacing_x):
            self.current_offset_x = -(self.width+2*spacing_x)
        self.current_offset_x += self.CURRENT_SPEED_X*time_factor

    def transform(self, x, y):
        x, y = self.tranform_perspective(x, y)
        # x, y = self.transform_2D(7x, y)
        return x, y


class GalaxyApp(App):
    pass


GalaxyApp().run()

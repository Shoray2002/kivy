from kivy.core.window import Window
from kivy import platform
from os import times
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics import Line, SmoothLine
from kivy.properties import Clock
from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')


class MainWidget(Widget):
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
        if self.is_desktop():
            self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self.keyboard.bind(on_key_down=self.on_key_down)
            self.keyboard.bind(on_key_up=self.on_key_up)

        Clock.schedule_interval(self.update, 1/60)

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

    def is_desktop(self):
        if platform in ['win', 'linux', 'macosx']:
            print("DESKTOP"+platform)
            return True
        return False

    def on_parent(self, *args):
        pass

    def on_size(self, *args):
        pass
        # self.update_vert_lines()
        # self.update_horizontal_lines()
        # print("ON SIZE WIDTH: "+str(self.width)+" HEIGHT: "+str(self.height))

        # def on_persepective_point_x(self, *args):
        #     print("ON PERSPECTIVE X: "+str(self.persepective_point_x))

        # def on_persepective_point_y(self, *args):
        #     print("ON PERSPECTIVE Y: "+str(self.persepective_point_y))

    def init_vert_lines(self):
        with self.canvas:
            # points=[self.width, 0, self.width, self.height], width=2)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(SmoothLine(width=1.1))

    def init_horizontal_lines(self):
        with self.canvas:
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(SmoothLine())

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

    def transform(self, x, y):
        x, y = self.tranform_perspective(x, y)
        # x, y = self.transform_2D(x, y)
        return x, y

    def transform_2D(self, x, y):
        return int(x), int(y)

    def tranform_perspective(self, x, y):
        lin_y = y*self.persepective_point_y/self.height
        if lin_y > self.persepective_point_y:
            lin_y = self.persepective_point_y
        diff_x = x-self.persepective_point_x
        diff_y = self.persepective_point_y-lin_y
        factor_y = diff_y/self.persepective_point_y
        factor_y = factor_y**4
        tr_x = self.persepective_point_x+diff_x*factor_y
        tr_y = self.persepective_point_y-factor_y*self.persepective_point_y
        return int(tr_x), int(tr_y)

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

    def on_touch_down(self, touch):
        if touch.x > self.width/2:
            self.CURRENT_SPEED_X = -self.SPEED_X
        else:
            self.CURRENT_SPEED_X = +self.SPEED_X

    def on_touch_up(self, touch):
        self.CURRENT_SPEED_X = 0


class GalaxyApp(App):
    pass


GalaxyApp().run()

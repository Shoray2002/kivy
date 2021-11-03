from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
# import line
from kivy.graphics import Line


class MainWidget(Widget):
    persepective_point_x = NumericProperty(0)
    persepective_point_y = NumericProperty(0)
    V_NB_LINES = 20
    V_LINES_SPACING = 0.1
    vertical_lines = []

    H_NB_LINES = 15
    H_LINES_SPACING = .1 
    horizontal_lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vert_lines()
        self.init_horizontal_lines()

    def on_parent(self, *args):
        pass

    def on_size(self, *args):
        self.update_vert_lines()
        self.update_horizontal_lines()
        # print("ON SIZE WIDTH: "+str(self.width)+" HEIGHT: "+str(self.height))

        # def on_persepective_point_x(self, *args):
        #     print("ON PERSPECTIVE X: "+str(self.persepective_point_x))

        # def on_persepective_point_y(self, *args):
        #     print("ON PERSPECTIVE Y: "+str(self.persepective_point_y))

    def init_vert_lines(self):
        with self.canvas:
            # points=[self.width, 0, self.width, self.height], width=2)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line(width=1.08))

    def init_horizontal_lines(self):
        with self.canvas:
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_vert_lines(self):
        central_line_x = int(self.width / 2)
        spacing = int(self.width * self.V_LINES_SPACING)
        central_line_x += spacing/2
        offset = -int(self.V_NB_LINES/2)
        for i in range(0, self.V_NB_LINES):
            line_x = int(central_line_x + (spacing)*offset)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def update_horizontal_lines(self):
        central_line_x = int(self.width / 2)
        spacing = self.V_LINES_SPACING * self.width
        offset = int(self.V_NB_LINES / 2) - 0.5

        xmin = central_line_x-offset*spacing
        xmax = central_line_x+offset*spacing
        spacing_y = self.H_LINES_SPACING*self.height

        for i in range(0, self.H_NB_LINES):
            line_y = i*spacing_y
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
        tr_y = y*self.persepective_point_y/self.height
        if tr_y > self.persepective_point_y:
            tr_y = self.persepective_point_y
        diff_x = x-self.persepective_point_x
        diff_y = self.persepective_point_y-tr_y
        factor_y = diff_y/self.persepective_point_y
        tr_x = self.persepective_point_x+diff_x*factor_y
        return int(tr_x), int(tr_y)


class GalaxyApp(App):
    pass


GalaxyApp().run()

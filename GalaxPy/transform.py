
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

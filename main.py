from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.metrics import dp 
from kivy.uix.pagelayout import PageLayout 
from kivy.properties import StringProperty,BooleanProperty,NumericProperty
from kivy.graphics.vertex_instructions import Line,Rectangle,Ellipse
from kivy.graphics.context_instructions import Color


class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super(StackLayoutEx, self).__init__(**kwargs)
        for i in range(1,101):
            b=Button(text=str(i),size_hint=(None,None),size=(dp(100),dp(100)))
            self.add_widget(b)
   

class WidgetExample(GridLayout):
    my_text = StringProperty('Hello')
    slider_value_txt=StringProperty('hello2')
    i=0
    count_enabled=BooleanProperty(False)
    switch_enabled=BooleanProperty(False)
    slider_value_num=NumericProperty(0)
    text_to_validate=StringProperty("")
    # input_text=StringProperty('Input\n Value')
    

    def on_btn_click_add(self,adder):
        # print('clicked '+str(self.i))
        if self.count_enabled:
            self.i+=1
            # adder.text='+'+str(self.i)
            self.my_text=str(self.i)
        
            print(adder.state)
    def on_btn_click_sub(self):
        print('clicked '+str(self.i))
        self.i-=1
        self.my_text=str(self.i)
    def on_toggle_btn(self,toggle):
        print('toggle '+ toggle.state)
        if toggle.state=='down':
            toggle.text='ON'
            self.count_enabled=True
        else:
            toggle.text='OFF'
            self.count_enabled=False
    def on_switch_active(self,switcher):
        print('switch '+ str(switcher.active))
        if switcher.active==True:
            self.switch_enabled=True
        else:
            self.switch_enabled=False
    # def on_slider_value(self,slider_ex):
    #     if self.switch_enabled==True:
    #         self.slider_value_txt=str(int(slider_ex.value))
    #         self.slider_value_num=int(slider_ex.value)
    def on_text_input_validate(self,validator):
        self.text_to_validate=validator.text



    
class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Color(1,0,0,1)
            Line(points=[0,0,100,100,200,0],width=5)
            self.rect=Rectangle(pos=(0,0),size=(100,100),source="./Images/4.png")
            Color(0,1,0,1)
            Line(rectangle=(100,100,100,100),width=5,)

    def on_click(self):
        # print('clicked')
        x,y=self.rect.pos
        x+=dp(10)
        y=y+dp(10)
        if x>self.width-dp(100) or y>self.height-dp(100):
            x=0
            y=0
        self.rect.pos=(x,y)

class CanvasExample3(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ball_size=dp(50)
        with self.canvas:
            self.ball=Ellipse(pos=self.center,size=(self.ball_size,self.ball_size))
    def on_size(self,*args):
        print("on size: "+str(self.width)+" , "+str(self.height))
        self.ball.pos=(self.center_x-self.ball_size/2,self.center_y-self.ball_size/2)













class Lab(App):
    pass

Lab().run()



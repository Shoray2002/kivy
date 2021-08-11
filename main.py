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
from kivy.properties import StringProperty


class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super(StackLayoutEx, self).__init__(**kwargs)
        for i in range(1,101):
            b=Button(text=str(i),size_hint=(None,None),size=(dp(100),dp(100)))
            self.add_widget(b)
   

# class GridLayoutEx(GridLayout):
#     pass

class WidgetExample(GridLayout):
    my_text = StringProperty('Hello')
    i=0
    def on_btn_click_add(self):
        print('clicked '+str(self.i))
        self.i+=1
        self.my_text=str(self.i)
    def on_btn_click_sub(self):
        print('clicked '+str(self.i))
        self.i-=1
        self.my_text=str(self.i)
    def on_toggle_btn(self):
        print('toggle')
    

# class BoxLayoutEx(BoxLayout):
#     pass
# class AnchorLayoutEx(AnchorLayout):
#     pass

# class CustomWidget(Widget):
#     pass

class Lab(App):
    pass

Lab().run()


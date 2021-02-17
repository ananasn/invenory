from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import ui


class MyApp(App):

    def print_str(self, str):
        print(str)
    # def build(self):
    #     return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
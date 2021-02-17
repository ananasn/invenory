from kivy.uix.textinput import TextInput
from kivy.properties import *


class NumericInput(TextInput):
    min_value = NumericProperty()
    max_value = NumericProperty()

    def __init__(self, *args, **kwargs):
        TextInput.__init__(self, *args, **kwargs)
        self.input_filter = 'float'
        self.multiline = False

    def insert_text(self, string, from_undo=False):
        new_text = self.text + string
        if new_text:
            if self.min_value <= float(new_text) <= self.max_value:
                TextInput.insert_text(self, string, from_undo=from_undo)

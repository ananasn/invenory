from kivy.app import App

from kivy_garden.xcamera import XCamera

import ui

from io import BytesIO
import base64


class MyXCamera(XCamera):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def shoot(self):
        img = self.export_as_image()
        buff = BytesIO()
        buff.seek(0)
        img.save(buff, fmt='png')
        with open('test.text', 'w') as f:
            f.write(base64.b64encode(buff.getvalue()).decode())
        print("Hello!")


class MyApp(App):

    def print_str(self, str):
        print(str)
    # def build(self):
    #     return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
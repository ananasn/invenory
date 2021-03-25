from kivy.app import App

from kivy_garden.xcamera import XCamera

import ui

from io import BytesIO
import base64
import requests

ADDR = 'http://127.0.0.1:8080/write'


class MyXCamera(XCamera):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.imageb64 = None

    def shoot(self):
        img = self.export_as_image()
        buff = BytesIO()
        buff.seek(0)
        img.save(buff, fmt='png')
        self.imageb64 = base64.b64encode(buff.getvalue()).decode()
        self.dispatch('on_picture_taken', 'success')


class MyApp(App):

    def send(self, data, photo):
        entry = {'entry_data': data, 'photo': photo}
        requests.post(ADDR, json=entry)
        print('Send!')


if __name__ == '__main__':
    MyApp().run()
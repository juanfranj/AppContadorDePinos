from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder

from libs.clases import *

class MainApp(MDApp):
    def build(self):
        Window.size = (450, 720)
        self.title = "ContadorDePinos"
        return Builder.load_file("main.kv")


MainApp().run()

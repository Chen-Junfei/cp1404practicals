from kivy.app import App
from kivy.lang import Builder


class Class(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('class.kv')
        return self.root


Class().run()
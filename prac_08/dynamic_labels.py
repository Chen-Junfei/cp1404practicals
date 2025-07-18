from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabels(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["A", "B", "C"]


    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
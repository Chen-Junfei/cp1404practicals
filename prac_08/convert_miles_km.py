from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


MILES_TO_KILOMETRES = 1.60934


class ConvertMilesToKilometres(App):
    result = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def press_convert(self,value):
        try:
            miles = float(value)
            km = miles * MILES_TO_KILOMETRES
            self.result = f"{km:2f}"
        except ValueError:
            self.result = "0.0"

    def press_up(self):
        try:
            current = float(self.root.ids.input_number.text)
            self.root.ids.input_number.text = str(current + 1)
        except ValueError:
            self.root.ids.input_number.text = "1"

    def press_down(self):
        try:
            current = float(self.root.ids.input_number.text)
            self.root.ids.input_number.text = str(current - 1)
        except ValueError:
            self.root.ids.input_number.text = "-1"


ConvertMilesToKilometres().run()

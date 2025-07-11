class Monitor:

    def __init__(self, model="", width=0, height=0):
        self.model = model
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.model}, width = {self.width}, height = {self.height}"

    def get_resolution(self) ->tuple:
        return self.width, self.height

    def get_total_pixels(self) ->int:
        return self.width * self.height

def main():
    x = Monitor("Monitor 1", 14, 22)
    print(x)
    print(x.get_resolution())
    print(x.get_total_pixels())


main()
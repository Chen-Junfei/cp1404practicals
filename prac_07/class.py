# class Monitor:
#
#     def __init__(self, model="", width=0, height=0):
#         self.model = model
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f"{self.model}, width = {self.width}, height = {self.height}"
#
#     def __eq__(self, other):
#         return self.width == other.width and self.height == other.height
#
#     def get_resolution(self) ->tuple:
#         return self.width, self.height
#
#     def get_total_pixels(self) ->int:
#         return self.width * self.height
#
# def main():
#     x = Monitor("Monitor 1", 14, 22)
#     print(x)
#     print(x.get_resolution())
#     print(x.get_total_pixels())
#     y = Monitor("Monitor 2", 14, 22)
#     print(x == y)
#
#
# main()


class User:

    def __init__(self, name):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def __str__(self):
        return f"{self.name}, {self.score} points, {self.number_of_tacos} tacos left"

    def give_tacos(self, other):
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            other.score += 1
        else:
            print("You have not taco to give")


def main():
    a = User("A")
    b = User("B")
    a.give_tacos(b)
    print(a)
    print(b)


main()
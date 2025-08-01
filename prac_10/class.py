# class Building:
#     def __init__(self, name = "", maximum_occupancy = 0 ):
#         self.name = name
#         self.maximum_occupancy = maximum_occupancy
#
#     def will_fit(self, number):
#         return self.maximum_occupancy >= number


# string = "CP1404 is good"
# words = string.split()
# words.reverse()
# print(" ".join(words))


# def create_dictionary(keys, values):
#     keys_to_values = {}
#     for i in range(len(keys)):
#         keys_to_values[keys[i]] = values[i]
#     return keys_to_values
#
# calories = [75,65,6175]
# food = ["1", "2", "3"]
# print(create_dictionary(food, calories))


# def do_thing(i):
#     return '*' * 2 * i
#
# for i in range(5):
#     print(do_thing(i))


# class A(object):
#     def __init__(self, data=1):
#         self.data = data
#
#     def getit(self):
#         return self.data * 2
#
# class T(A):
#     def __init__(self, value=3):
#         super().__init__(value * 2)
#
# a, b = A(2), T()
# print(a.getit(), b.getit())
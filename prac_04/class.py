# names = ['Ada', 'Alan', 'Bill', 'John']
# print(",".join(names))
# name_to_remove = input("Who do you want to remove? ").strip()
# while name_to_remove != '':
#     try:
#         names.remove(name_to_remove)
#     except ValueError:
#         print("Value Error, enter again.")
#     print(",".join(names))
#     name_to_remove = input("Who do you want to remove? ").strip()


# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
# def get_numbers():
#     numbers = input("Enter numbers separated by commas: ").split(",")
#     return [float(number) for number in numbers]
#
# def square_numbers(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] ** 2
#
# def display_numbers(numbers):
#     sorted_numbers = sorted(numbers)
#     print(sorted_numbers)
#
# main()


# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# max_len_of_name = max([len(pair[0]) for pair in data])
# max_len_of_number = max([len(str(pair[1])) for pair in data])
# for pair in data:
#     name, score = pair
#     print(f"{name:{max_len_of_name}}={score:{max_len_of_number}}")


# print(isinstance(True,int))

# values = [[3,4,5,6],[33,6,1,2]]
# v = 3
# print(values[0][0])
# for row in range(len(values)):
#     for column in range(len(values[row])):
#         if v < values[row][column]:
#             v = values[row][column]
# print(v)

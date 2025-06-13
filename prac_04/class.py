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

def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)

def get_numbers():
    numbers = input("Enter numbers separated by commas: ").split(",")
    return [float(number) for number in numbers]

def square_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2

def display_numbers(numbers):
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)

main()
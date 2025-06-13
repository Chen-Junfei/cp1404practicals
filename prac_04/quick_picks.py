import random
NUMBER_OF_COLUMN = 6


def main():
    """The main entry point of the program."""
    number_of_quick_pick = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(number_of_quick_pick)
    display_quick_picks(quick_picks)


def generate_quick_picks(number_of_quick_pick):
    """Generate a list of random numbers based on the number of lines provided by the user."""
    quick_picks = []
    for row in range(number_of_quick_pick):
        rows = []
        for column in range(NUMBER_OF_COLUMN):
            number = random.randint(1, 45)
            while number in rows:  # Check if the random number is any repeated number
                number = random.randint(1, 45)
            rows.append(number)
        rows.sort()
        quick_picks.append(rows)
    return quick_picks


def display_quick_picks(quick_picks):
    """Display the random list."""
    for row in range(len(quick_picks)):
        for column in range(len(quick_picks[row])):
            print(f"{quick_picks[row][column]:2}", end=" ")
        print()

main()
from guitar import Guitar


def main():
    """Read file of guitar details, save as a list of objects, display."""
    my_guitars = []
    in_file = open("guitars.csv", 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        my_guitars.append(guitar)
    in_file.close()

    for guitar in my_guitars:
        print(guitar)
    print()

    my_guitars.sort()
    for guitar in my_guitars:
        print(guitar)

main()
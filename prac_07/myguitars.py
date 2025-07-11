from guitar import Guitar
import csv


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

    add_guitar(my_guitars)


def add_guitar(my_guitars):
    name = input("Name: ")
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitar = Guitar(name, year, cost)
    print(guitar)
    my_guitars.append(guitar)
    out_file = open("guitars.csv",'w', newline='')
    writer = csv.writer(out_file)
    for guitar in my_guitars:
        writer.writerow([guitar.name, guitar.year, guitar.cost])
    out_file.close()


main()
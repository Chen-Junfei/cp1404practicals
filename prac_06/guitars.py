"""
Word Occurrences
Estimate: 5 minutes
Actual:   13 minutes
"""

from guitar import Guitar


def main():
    """Record and display my guitar"""
    guitars = []
    print("My guitars!")

    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost} added")

    print("\n... snip ...\n")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()
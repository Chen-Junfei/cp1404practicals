"""
Word Occurrences
Estimate: 30 minutes
Actual:   33 minutes
"""


FILENAME = "wimbledon.csv"

def main():
    """Carry out the main part of the program and link the corresponding functions"""
    data_list = load_file()
    name_to_times = get_dictionary(data_list)
    print("Wimbledon Champions: ")
    for name, times in name_to_times.items():
        print(f"{name} {times}")
    countries = get_country_list(data_list)
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_file():
    """Load file to return a list for main function"""
    champions = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.split(",")[1:3]
            champions.append(parts)
    return champions


def get_dictionary(data_list):
    """generate a dictionary to record name and champion times"""
    name_to_times = {}
    for data in data_list:
        name_to_times[data[1]] = name_to_times.get(data[1],0) + 1
    return name_to_times


def get_country_list(data_list):
    """Return a set that records the countries of the championship-winning players"""
    return set([data[0] for data in data_list])


main()
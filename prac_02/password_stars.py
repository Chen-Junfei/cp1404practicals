MIN_LENGTH = 6
def main():
    """main function"""
    password = get_password()
    print_stars(password)


def print_stars(password):
    print("*" * len(password))


def get_password():
    password = str(input("Enter password: "))
    while len(password) < MIN_LENGTH:
        print("Invalid password.")
        password = str(input("Enter password: "))
    return password


main()
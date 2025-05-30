MIN_LENGTH = 6
def main():
    """main function"""
    password = str(input("Enter password: "))
    while len(password) < MIN_LENGTH:
        print("Invalid password.")
        password = str(input("Enter password: "))
    print("*" * len(password))

main()
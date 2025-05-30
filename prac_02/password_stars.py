MIN_LENGTH = 6
def main():
    """main function"""
    password = str(input("Enter password: "))
    while is_valid_password(password) == False:
        print("Invalid password.")
        password = str(input("Enter password: "))
    print("*" * len(password))

main()
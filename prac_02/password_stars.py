MIN_LENGTH = 6
def main():
    """main function"""
    password = str(input("Enter password: "))
    while is_valid_password(password) == False:
        print("Invalid password.")
        password = str(input("Enter password: "))
    print("*" * len(password))

def is_valid_password(password):
    """check whether the password is valid"""
    return len(password) >= MIN_LENGTH

main()
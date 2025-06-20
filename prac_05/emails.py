"""
Word Occurrences
Estimate: 20 minutes
Actual:   13 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        choice = input(f"Is your name {name}? (Y/n) ")
        if choice.upper() != "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    name = email.split("@")[0]
    return ' '.join(name.split(".")).title()


main()


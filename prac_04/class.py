names = ['Ada', 'Alan', 'Bill', 'John']
print(",".join(names))
name_to_remove = input("Who do you want to remove? ").strip()
while name_to_remove != '':
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("Value Error, enter again.")
    print(",".join(names))
    name_to_remove = input("Who do you want to remove? ").strip()

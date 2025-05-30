MANU = """(H)ello
(G)oodbye
(Q)uit"""
name = str(input("Enter name: "))
print(MANU)
choice = str(input(">>> "))
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MANU)
    choice = str(input(">>> "))
print("Finished")

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

def main():
    """main function"""
    score = get_score()
    print(MENU)
    choice = str(input(">>> ")).upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
            print(f"Your score is {score}")
        elif choice == "P":
            result = get_result(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = str(input(">>> ")).upper()
    print("Bye.")

def get_score():
    """get and return a valid score"""
    score = int(input("Enter score: "))
    while score <0 or score >100:
        print("Invalid score.")
        score = int(input("Enter score: "))
    return score

def get_result(score):
    """get result from score"""
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score <= 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"
    else:
        return "Invalid score"

def print_stars(score):
    print("*" * score)

main()
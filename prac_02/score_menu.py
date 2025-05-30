from prac_02.password_stars import print_stars
from prac_02.score import get_result

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

def main():
    """main function"""
    print(MENU)
    choice = str(input(">>> ")).upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
            print(f"Your score is {score}")
        elif choice == "P":
            if score == "":
                print("Please Enter your score first.")
            else:
                result = get_result()
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = str(input(">>> ")).upper()
    print("Bye.")
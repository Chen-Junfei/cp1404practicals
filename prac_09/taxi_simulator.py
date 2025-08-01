from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_cost = drive_taxi(current_taxi)
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input; enter a number.")
        return None


def drive_taxi(taxi):
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid input; drive cancelled.")
        return 0.0

    taxi.start_fare()
    taxi.drive(distance)
    return taxi.get_fare()


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()
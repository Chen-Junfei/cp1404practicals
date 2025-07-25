from unreliable_car import UnreliableCar

def test_unreliable_car():
    reliable_car = UnreliableCar("ReliableCar", 1000, 90)
    unreliable_car = UnreliableCar("UnreliableCar", 1000, 30)

    drive_attempts = 100
    drive_distance = 10

    reliable_success = 0
    unreliable_success = 0

    for _ in range(drive_attempts):
        if reliable_car.drive(drive_distance) > 0:
            reliable_success += 1
        if unreliable_car.drive(drive_distance) > 0:
            unreliable_success += 1

    print(f"ReliableCar successful drives: {reliable_success}/{drive_attempts}")
    print(f"UnreliableCar successful drives: {unreliable_success}/{drive_attempts}")

test_unreliable_car()
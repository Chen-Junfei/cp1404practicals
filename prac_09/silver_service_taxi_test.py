from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    taxi_1 = SilverServiceTaxi("Taxi 1", 200, 2.0)
    taxi_1.drive(18)
    fare = taxi_1.get_fare()

    print(taxi_1)
    print(f"Fare for 18km: ${fare:.2f}")

    # assert fare == 48.78, f"Expected fare to be 48.78, but got {fare}"

test_silver_service_taxi()
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        fare = super().get_fare() + SilverServiceTaxi.flagfall
        return fare

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"
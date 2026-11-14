from Chumachenko import Station
from Sulymenko import Client
from Kravchenko import Bike

class Result:
    def __init__(self, is_success: bool, error_message: str):
        self.is_success = is_success
        self.error_message = error_message

class RentalService:
    def __init__(self) -> None:
        self._total_revenue: float = 0.0

    @property
    def total_revenue(self):
        return self._total_revenue

    def calculate_cost(self, bike: Bike, minutes: int) -> float:
        return bike.get_rate() * minutes

    def rent_bike(self, client: Client, station: Station, bike: type[Bike] | None = None) -> Result | None:
        pass

    def return_bike(self, client: Client, station: Station, minutes: int) -> Result:
        pass

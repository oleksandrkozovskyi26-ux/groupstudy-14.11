from Chumachenko import Station
from Sulymenko import Client
from Kravchenko import Bike

class Result:
    def __init__(self, is_success: bool, error_message: str = ""):
        self.is_success = is_success
        self.error_message = error_message

class RentalService:
    def __init__(self) -> None:
        self._total_revenue: float = 0.0

    @property
    def total_revenue(self):
        return self._total_revenue

    def rent_bike(self, client: Client, station: Station, bike_type: type[Bike] | None = None) -> Result | None:
        if client.has_bike():
            return Result(False, f"{client.name} уже орендує велосипед")

        if client.balance <= 0:
            return Result(False, f"У клієнта {client.name} недостатньо коштів")

        selected_bike: Bike | None = None
        for bike in station.bikes:
            if bike_type is None or isinstance(bike, bike_type):
                selected_bike = bike
                break

        if selected_bike is None:
            return Result(False, f"На станції '{station.name}' немає вільних велосипедів")

        station.remove_bike(selected_bike)
        client.assign_bike(selected_bike)
        return Result(True)

    def return_bike(self, client: Client, station: Station, minutes: int) -> Result:
        if not client.has_bike():
            return Result(False, f"У клієнта {client.name} немає активної оренди")

        if minutes <= 0:
            return Result(False, "Тривалість поїздки має бути більшою за 0 хв")

        current_bike: Bike = client.current_bike
        cost: float = float(current_bike.rent(minutes))

        if not client.charge(cost):
            return Result(False, f"Недостатньо коштів. Потрібно {cost:.0f} грн, на балансі {client.balance:.0f} грн")

        client.remove_bike()
        station.add_bike(current_bike)
        self._total_revenue += cost

        return Result(True)

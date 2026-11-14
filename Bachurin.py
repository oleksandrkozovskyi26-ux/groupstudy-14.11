from Chumachenko import Station
from Sulymenko import Client
from Kravchenko import Bike

class Result:
    def __init__(self, is_success: bool, error_message: str):
        self.is_success = is_success
        self.error_message = error_message

class RentalService:
    def __init__(self) -> None:
        ...



from dataclasses import dataclass
from datetime import datetime

@dataclass
class Flight:
    _id: int
    _airline_id: int
    _flight_number: int
    _tail_number: int
    _origin_airport_id: int
    _destination_airport_id: int
    _scheduled_departure_date: datetime
    _departure_delay: int
    _elapsed_time: int
    _distance: int
    _arrival_date: datetime
    _arrival_delay: int

    def __str__(self):
        return f"{self._id}-{self._airline_id}-{self._flight_number}"

    def __hash__(self):
        return hash(self._id)
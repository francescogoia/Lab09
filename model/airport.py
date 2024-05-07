from dataclasses import dataclass


@dataclass
class Airport:
    _id: int
    _iata_code: str
    _airport: str
    _city: str
    _state: str
    _country: str
    _latitude: int
    _longitude: int
    _timezone_offset: int

    def __str__(self):
        return f"{self._id}-{self._iata_code}-{self._city}-{self._state}-{self._country}"

    def __repr__(self):
        return f"{self._id}-{self._iata_code}-{self._airport}-{self._city}-{self._state}-{self._country}"

    def __hash__(self):
        return hash(self._id)
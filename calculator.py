import math
from datetime import datetime


def landing_fee(mtow_kg: float) -> float:
    if mtow_kg <= 2000:
        return 75.0
    tons = math.ceil(mtow_kg / 1000)
    return tons * 25.0


def passenger_fee(passengers: int) -> float:
    return passengers * 57.14


def parking_duration_hours(arrival: datetime, departure: datetime) -> float:
    delta = departure - arrival
    return round(delta.total_seconds() / 3600, 1)


def parking_fee(mtow_kg: float, arrival: datetime, departure: datetime) -> float:
    hours = parking_duration_hours(arrival, departure)

    if hours <= 4:
        return 0.0

    days = math.ceil(hours / 24)
    tons = math.ceil(mtow_kg / 1000)

    return days * tons * 4.5


def calculate_all(passengers: int, mtow_kg: float,
                  arrival: datetime, departure: datetime) -> dict:
    landing = landing_fee(mtow_kg)
    pax_fee = passenger_fee(passengers)
    parking = parking_fee(mtow_kg, arrival, departure)
    duration = parking_duration_hours(arrival, departure)

    total = landing + pax_fee + parking

    return {
        "input": {
            "passengers": passengers,
            "mtow": mtow_kg,
            "duration_hours": duration
        },
        "fees": {
            "landing": round(landing, 2),
            "passengers": round(pax_fee, 2),
            "parking": round(parking, 2),
            "total": round(total, 2)
        }
    }

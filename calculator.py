from datetime import datetime
from math import ceil

def calculate_fees(passengers, mtow, arrival, departure):
    """
    Funkcja liczy opłaty lotniskowe:
    - lądowanie
    - pasażerowie odlatujący
    - postój
    """
    # --- OPŁATA ZA LĄDOWANIE ---
    if mtow <= 2000:
        landing_fee = 75.0
    else:
        # każda rozpoczęta tona powyżej 2 ton, 25 PLN za tonę
        landing_fee = ceil(mtow / 1000) * 25.0

    # --- OPŁATA ZA PASAŻERA ODLATUJĄCEGO ---
    passenger_fee = passengers * 57.14

    # --- OPŁATA ZA POSTÓJ ---
    # przelicz daty na datetime
    fmt = "%Y-%m-%dT%H:%M"
    try:
        arrival_dt = datetime.strptime(arrival, fmt)
        departure_dt = datetime.strptime(departure, fmt)
        duration = departure_dt - arrival_dt
        duration_hours = duration.total_seconds() / 3600
    except:
        duration_hours = 0

    if duration_hours <= 4:
        parking_fee = 0.0
    else:
        days = ceil(duration_hours / 24)
        parking_fee = days * ceil(mtow / 1000) * 4.5

    # suma wszystkich opłat
    total = landing_fee + passenger_fee + parking_fee

    # zwracamy szczegółową strukturę
    return {
        "input": {
            "passengers": passengers,
            "mtow": mtow,
            "duration_hours": duration_hours
        },
        "fees": {
            "landing": landing_fee,
            "passengers": passenger_fee,
            "parking": parking_fee,
            "total": total
        }
    }

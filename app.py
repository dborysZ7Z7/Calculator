import os
from flask import Flask, render_template, request
from calculator import calculate_fees  # Twój moduł z funkcją obliczeń

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    form = {}
    if request.method == "POST":
        try:
            # Pobranie danych z formularza
            passengers = int(request.form["passengers"])
            mtow = float(request.form["mtow"])
            arrival = request.form["arrival"]
            departure = request.form["departure"]

            form = {
                "passengers": passengers,
                "mtow": mtow,
                "arrival": arrival,
                "departure": departure
            }

            # Wywołanie funkcji obliczającej opłaty
            result = calculate_fees(passengers, mtow, arrival, departure)

        except Exception as e:
            # Jeśli coś pójdzie nie tak, wynik pozostaje None
            print("Błąd:", e)
            result = None

    return render_template("index.html", result=result, form=form)


if __name__ == "__main__":
    # Railway ustawia port w zmiennej środowiskowej PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

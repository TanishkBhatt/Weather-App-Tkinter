from config import API_KEY
import requests

def getData(city: str) -> dict:
    """Fuction that fetches data from the server"""
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        res = requests.get(url)
        if (res.status_code != 200):
            return {}
        res = res.json()

        summary = {
            "CITY": res["name"],
            "WEATHER": res["weather"][0]["main"],
            "TEMPERATURE": res["main"]["temp"],
            "FEELS_LIKE": res["main"]["feels_like"],
            "HUMIDITY": res["main"]["humidity"],
            "WIND_SPEED": res["wind"]["speed"],
            "ICON": res["weather"][0]["icon"]
        }
        return summary

    except Exception:
        return {}
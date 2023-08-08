import requests
import pyttsx3

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
        "lang": "tr"
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        rain = "Yağmur yağıyor." if "rain" in data else "Yağmur yağmıyor."
        return {
            "description": weather_description,
            "temperature": temperature,
            "wind_speed": wind_speed,
            "humidity": humidity,
            "rain": rain
        }
    else:
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    city_name = "ANKARA"  # Hava durumu bilgisini öğrenmek istediğiniz şehir adını buraya yazabilirsiniz.
    api_key = "Openweathermap api"  # OpenWeatherMap API anahtarınızı buraya yazınız.

    weather_data = get_weather(city_name, api_key)
    if weather_data:
        print(f"Hava Durumu: {weather_data['description']}")
        print(f"Sıcaklık: {weather_data['temperature']} °C")
        print(f"Rüzgar Hızı: {weather_data['wind_speed']} m/s")
        print(f"Nem Oranı: {weather_data['humidity']} %")
        print(weather_data['rain'])

        speak(f"{city_name} şehrinde hava durumu: {weather_data['description']}. Sıcaklık: {weather_data['temperature']} derece Celsius. Rüzgar hızı: {weather_data['wind_speed']} metre/saniye. Nem oranı: {weather_data['humidity']} yüzde. {weather_data['rain']}")
    else:
        print("Hava durumu bilgisi alınamadı.")

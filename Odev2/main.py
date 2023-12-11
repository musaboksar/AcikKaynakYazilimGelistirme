import requests
import keyboard

API_KEY = "6114a2c6aac933789d6b2523351993a4"

city = input("Sehir: ")

while True:
    if(keyboard.is_pressed("Enter")):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&&lang=tr")
        data = response.json()
        print("Hava durumu bilgileri: ", data["weather"][0])
        break

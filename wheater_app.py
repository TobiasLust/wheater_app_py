import requests


class Wheater:
    api_key = "5183fe7ad30d48cc9ea215648242808"

    def __init__(self):
        self.city: str = ""
        self.country: str = ""
        self.celcius: float = 0
        self.feelslike_c: float = 0
        self.local_time: str = ""
        self.state:str = ""
        self.clouds: float = 0
        self.humidity: float = ""

    def __str__(self) -> str:
        return f"""Hoy: {self.local_time} en {self.city} {self.country}
    ----
    {self.celcius}C
    Sensacion termica: {self.feelslike_c}C
    Clima: {self.state}
    Humedad: {self.humidity}%
    Nubes: {self.clouds}%
    """

    def get_city(self, city: str):

        res = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={Wheater.api_key}&q={city}&aqi=no"
        )
        if res.status_code == 400:
            res = res.json()
            raise requests.exceptions.RequestException(f'{res["error"]["message"]}')

        res = res.json()
        self.city = city.title()
        self.country = res["location"]["country"]
        self.local_time = res["location"]["localtime"]
        self.celcius = res["current"]["temp_c"]
        self.feelslike_c = res["current"]["feelslike_c"]
        self.state = res["current"]["condition"]["text"]
        self.humidity = res["current"]["humidity"]
        self.clouds = res["current"]["cloud"]


def main():
    city = Wheater()
    try:
        city.get_city(input("City: "))
        print(city)
    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    main()

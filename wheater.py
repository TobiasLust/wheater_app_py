import requests


class Wheater:
    api_key = "5183fe7ad30d48cc9ea215648242808"

    def __init__(self):
        self.city: str = ""
        self._country: str = ""
        self._celcius: float = 0
        self._feelslike_c: float = 0
        self._local_time: str = ""
        self._state: str = ""
        self._clouds: float = 0
        self._humidity: float = ""


    def get_city(self, city: str):

        res = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={Wheater.api_key}&q={city}&aqi=no"
        )
        if res.status_code == 400:
            res = res.json()
            raise requests.exceptions.RequestException(f'{res["error"]["message"]}')

        res = res.json()
        self.city = res["location"]["name"]
        self._country = res["location"]["country"]
        self._local_time = res["location"]["localtime"]
        self._celcius = res["current"]["temp_c"]
        self._feelslike_c = res["current"]["feelslike_c"]
        self._state = res["current"]["condition"]["text"]
        self._humidity = res["current"]["humidity"]
        self._clouds = res["current"]["cloud"]

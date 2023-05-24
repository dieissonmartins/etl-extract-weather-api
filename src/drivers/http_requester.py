from typing import Dict
from .interfaces.http_requester import HttpRequesterInterface
from dotenv import load_dotenv
import os
import requests


class HttpRequester(HttpRequesterInterface):
    __url: str
    __headers: Dict
    __params: Dict
    __key: str
    __prefix: str

    def __init__(self) -> None:
        # load envs
        load_dotenv()

        # base url
        self.__url = 'https://weather.visualcrossing.com'

        # set prefix
        self.__prefix = '/VisualCrossingWebServices/rest/services/timeline'

        # set headers
        self.__headers = {'content-type': 'application/json'}

        # key token acess
        self.__key = os.getenv("KEY")

    def get_weather_by_city(self) -> Dict[str, str | int]:
        city = 'Rio de Janeiro'
        dt_start = '2022-01-01'
        dt_end = '2022-02-01'

        endpoint = f'{self.__url}{self.__prefix}/{city}/{dt_start}/{dt_end}'

        params = {
            'unitGroup': 'us',
            'contentType': 'json',
            'include': 'current,alerts',
            'key': self.__key
        }

        response = requests.get(endpoint, params)

        data = response.json()

        ret = {
            "status_code": response.status_code,
            "data": data
        }

        return ret

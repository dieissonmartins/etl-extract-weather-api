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
        endpoint = self.__url + self.__prefix + '/Rio de Janeiro/2022-01-01/2022-02-01'

        params = '?unitGroup=us&contentType=json&include=current,alerts&key=' + self.__key

        response = requests.get(endpoint, params)

        ret = {
            "status_code": response.status_code,
            "data": response.content
        }

        return ret

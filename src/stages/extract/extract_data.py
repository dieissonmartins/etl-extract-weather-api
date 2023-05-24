from src.drivers.interfaces.http_requester import HttpRequesterInterface
from src.errors.extract_error import ExtractError
from mss import exception
from typing import Dict


class ExtractData:
    def __init__(self, http_requester: HttpRequesterInterface):
        self.__http_requester = http_requester

    def extract(self) -> Dict[str, str | int]:
        try:
            data = self.__http_requester.get_weather_by_city()

            ret = data

            return ret

        except Exception as e:
            raise ExtractError(str(e)) from exception

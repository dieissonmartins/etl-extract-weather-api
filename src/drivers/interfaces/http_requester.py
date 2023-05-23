from abc import ABC, abstractmethod
from typing import Dict


class HttpRequesterInterface(ABC):

    @abstractmethod
    def get_weather_by_city(self) -> Dict[str, str | int]:
        pass

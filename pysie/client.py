from typing import Dict

import requests

from .constants import Conf, Series
from .settings import API_KEY


class SIE:
    base_url: str
    headers: Dict

    def __init__(self):
        self.base_url = Conf.BASE_URL.value
        self.headers = {"Bmx-Token": API_KEY}

    def _manage_request(self, serie: str):
        url: str = f"{self.base_url}/series/{serie}/datos/oportuno"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()["bmx"]["series"][0]


def make_get_serie(method_name, serie_value):
    def _get_serie(self):
        return self._manage_request(serie_value)

    _get_serie.__name__ = method_name
    return _get_serie


series_methods = {
    "get_cetes": Series.CETES.value,
    "get_dollar_price": Series.DOLLAR_PRICE.value,
    "get_inflation": Series.INFLATION.value,
    "get_tiie": Series.TIIE.value,
    "get_udi": Series.UDI.value,
    "get_yield_target": Series.YIELD_TARGET.value,
}

for method_name, serie_value in series_methods.items():
    setattr(SIE, method_name, make_get_serie(method_name, serie_value))

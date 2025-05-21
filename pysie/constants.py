from enum import Enum


class Conf(Enum):
    BASE_URL: str = "https://www.banxico.org.mx/SieAPIRest/service/v1"


class Series(Enum):
    CETES: str = "SF43936"
    DOLLAR_PRICE: str = "SF43718"
    INFLATION: str = "SP74665"
    TIIE: str = "SF331451"
    UDI: str = "SP68257"
    YIELD_TARGET: str = "SF61745"

from enum import Enum


class Conf(Enum):
    BASE_URL: str = "https://www.banxico.org.mx/SieAPIRest/service/v1"


class Series(Enum):
    CETES: str = "SF43936"
    COUNTERFEIT_BILLS: str = "SM1255"
    COUNTERFEIT_BILLS_20: str = "SM1249"
    COUNTERFEIT_BILLS_50: str = "SM1250"
    COUNTERFEIT_BILLS_100: str = "SM1251"
    COUNTERFEIT_BILLS_200: str = "SM1252"
    COUNTERFEIT_BILLS_500: str = "SM1253"
    COUNTERFEIT_BILLS_1000: str = "SM1254"
    DOLLAR_EXCHANGE_RATE: str = "SF43718"
    INFLATION: str = "SP74665"
    TIIE: str = "SF331451"
    UDI: str = "SP68257"
    USED_CREDIT_CARDS: str = "SF61872"
    USED_DEBIT_CARDS: str = "SF61873"
    YIELD_TARGET: str = "SF61745"

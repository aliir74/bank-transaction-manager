import requests
from django.conf import settings
from currencyExchange.repositories import CurrencyExchange


class ExchangerRatesAPIIO(CurrencyExchange):

    @staticmethod
    def _get_rates_from_api():
        url = f"http://api.exchangeratesapi.io/v1/latest?access_key={settings.EXCHANGE_API_ACCESS_KEY}&sybmols=USD"

        response = requests.get(url=url).json()
        eur_to_usd = response['rates']['USD']
        usd_to_eur = 1. / eur_to_usd

        return eur_to_usd, usd_to_eur

    @property
    def redis_key_prefix(self):
        return 'exchange_api:'

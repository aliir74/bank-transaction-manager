import decimal
from abc import ABC, abstractmethod
import redis
from django.conf import settings
from typing import Tuple


class CurrencyExchange(ABC):
    redis_client = redis.Redis(settings.REDIS['HOST'], settings.REDIS['PORT'])

    def _set_rates_to_redis(self, eur_to_usd, usd_to_eur):
        self.redis_client.set(self.eur_to_usd_key, eur_to_usd, ex=settings.EXCHANGE_API_CACHE_SECONDS)
        self.redis_client.set(self.usd_to_eur_key, usd_to_eur, ex=settings.EXCHANGE_API_CACHE_SECONDS)

    @staticmethod
    @abstractmethod
    def _get_rates_from_api() -> Tuple[float, float]:
        """
        :return: eur_to_usd and usd_to_eur rates
        """
        pass

    @property
    def eur_to_usd(self):
        if self.redis_client.exists(self.eur_to_usd_key):
            eur_to_usd = self.redis_client.get(self.eur_to_usd_key)
        else:
            eur_to_usd, usd_to_eur = self._get_rates_from_api()
            self._set_rates_to_redis(eur_to_usd, usd_to_eur)
        return decimal.Decimal(float(eur_to_usd))

    @property
    def usd_to_eur(self):
        if self.redis_client.exists(self.usd_to_eur_key):
            usd_to_eur = self.redis_client.get(self.usd_to_eur_key)
        else:
            eur_to_usd, usd_to_eur = self._get_rates_from_api()
            self._set_rates_to_redis(eur_to_usd, usd_to_eur)
        return decimal.Decimal(float(usd_to_eur))

    @property
    @abstractmethod
    def redis_key_prefix(self):
        pass

    @property
    def eur_to_usd_key(self):
        return self.redis_key_prefix+'eur_to_usd'

    @property
    def usd_to_eur_key(self):
        return self.redis_key_prefix+'usd_to_eur'

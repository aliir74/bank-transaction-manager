from django.db import models
from bankAccounts.models.base import BaseMoneyModel
from bankAccounts.models.account import Account
from currencyExchange.repositories.exchangeratesapiio import ExchangerRatesAPIIO
from django.db import transaction


class Transaction(BaseMoneyModel):
    class ThirdPartyAPI(models.TextChoices):
        default = '1', 'exchangeratesapi.io'  # TODO: pick some third party api for default
    comment = models.CharField(max_length=200, blank=True)
    from_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='from_transactions')
    to_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='to_transactions')
    third_party_api = models.CharField(max_length=20, blank=True, choices=ThirdPartyAPI.choices,
                                       default=ThirdPartyAPI.default)

    @transaction.atomic
    def save(self, *args, **kwargs):
        exchanger = ExchangerRatesAPIIO()
        self.from_account.decrease_balance(self.balance, self.currency, exchanger)
        self.to_account.increase_balance(self.balance, self.currency, exchanger)
        super().save(*args, **kwargs)


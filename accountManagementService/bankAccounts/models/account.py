from django.db import models
from bankAccounts.models.base import BaseMoneyModel, Currency
from currencyExchange.repositories import CurrencyExchange


class Account(BaseMoneyModel):
    passport_id = models.CharField(max_length=20, null=False, blank=False)

    def _exchange_currency(self, input_balance, input_currency: Currency, exchanger: CurrencyExchange):
        exchange_rate = 1
        if input_currency != self.currency:
            if input_currency == Currency.USD:
                exchange_rate = exchanger.usd_to_eur
            elif input_currency == Currency.EUR:
                exchange_rate = exchanger.eur_to_usd
        input_balance *= exchange_rate
        return input_balance

    def increase_balance(self, input_balance, input_currency: Currency, exchanger: CurrencyExchange):
        input_balance = self._exchange_currency(input_balance, input_currency, exchanger)
        self.balance += input_balance
        self.save()

    def decrease_balance(self, input_balance, input_currency: Currency, exchanger: CurrencyExchange):
        input_balance = self._exchange_currency(input_balance, input_currency, exchanger)
        if self.balance - input_balance >= 0:
            self.balance -= input_balance
        else:
            raise ValueError("Negative balance error")
        self.save()

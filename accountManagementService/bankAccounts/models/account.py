from django.db import models
from bankAccounts.models.base import BaseMoneyModel, Currency


class Account(BaseMoneyModel):
    passport_id = models.CharField(max_length=20, null=False, blank=False)

    def increase_balance(self, input_balance, input_currency: Currency):
        if input_currency == self.currency:
            self.balance += input_balance
        else:
            pass
            # TODO:handle currency exchange
        self.save()

    def decrease_balance(self, input_balance, input_currency: Currency):
        if input_currency == self.currency:
            if self.balance - input_balance >= 0:
                self.balance -= input_balance
            else:
                raise ValueError
        else:
            pass
            # TODO:handle currency exchange
        self.save()

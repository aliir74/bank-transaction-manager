from django.db import models
from bankAccounts.models.base import BaseModel


class Account(BaseModel):
    class Currency(models.TextChoices):
        USD = 'USD', 'USD'
        EUR = 'EUR', 'EUR'

    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, choices=Currency.choices, default=Currency.USD, null=False, blank=False)
    passport_id = models.CharField(max_length=20, null=False, blank=False)

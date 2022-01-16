from django.db import models
from bankAccounts.models.base import BaseModel
from bankAccounts.models.user import User


class Account(BaseModel):
    class Currency(models.TextChoices):
        USD = 'USD', 'USD'
        EUR = 'EUR', 'EUR'

    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, choices=Currency.choices, default=Currency.USD, null=False, blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='accounts', blank=True)

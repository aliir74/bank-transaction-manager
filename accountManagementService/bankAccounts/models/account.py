from django.db import models
from bankAccounts.models.base import BaseModel
from bankAccounts.models.user import User


class Account(BaseModel):
    class Currency(models.TextChoices):
        USD = '1', 'USD'
        EUR = '2', 'EUR'

    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, choices=Currency.choices, default=Currency.USD)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='accounts')

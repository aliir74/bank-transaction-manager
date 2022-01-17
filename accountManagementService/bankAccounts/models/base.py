from django.db import models


class DateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class BaseModel(DateModel):

    class Meta:
        abstract = True


class Currency(models.TextChoices):
    USD = 'USD', 'USD'
    EUR = 'EUR', 'EUR'


class BaseMoneyModel(BaseModel):

    balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, choices=Currency.choices, default=Currency.USD, null=False, blank=False)

    class Meta:
        abstract = True

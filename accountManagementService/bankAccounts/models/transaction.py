from django.db import models
from bankAccounts.models.base import BaseModel
from bankAccounts.models.account import Account


class Transaction(BaseModel):
    class ThirdPartyAPI(models.TextChoices):
        default = '1', 'default'  # TODO: pick some third party api for default
    comment = models.CharField(max_length=200, blank=True)
    from_account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='from_transactions')
    to_account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name='to_transactions')
    third_party_api = models.CharField(max_length=20, blank=True, choices=ThirdPartyAPI.choices,
                                       default=ThirdPartyAPI.default)

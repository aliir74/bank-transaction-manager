from django.db import models
from bankAccounts.models.base import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=100, null=True)
    passport_id = models.CharField(max_length=15, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
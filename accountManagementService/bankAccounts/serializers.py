from rest_framework import serializers
from bankAccounts.models import Account, User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'balance', 'currency', 'user']


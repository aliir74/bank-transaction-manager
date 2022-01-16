from rest_framework import serializers
from bankAccounts.models import Account, User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'balance', 'currency', 'created_at', 'updated_at']
        # TODO: handle user in requests

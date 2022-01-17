from rest_framework import serializers
from bankAccounts.models import Transaction, User


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'comment', 'from_account_id', 'to_account_id', 'third_party_api',
                  'created_at', 'updated_at']


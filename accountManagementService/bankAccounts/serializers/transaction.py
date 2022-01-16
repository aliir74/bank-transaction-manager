from rest_framework import serializers
from bankAccounts.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'comment', 'from_user', 'to_user', 'third_party_api', 'created_at', 'updated_at']
        # TODO: handle user in requests


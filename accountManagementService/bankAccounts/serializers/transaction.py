from rest_framework import serializers
from bankAccounts.models import Transaction, Account
from bankAccounts.models.base import Currency


class TransactionSerializer(serializers.ModelSerializer):
    from_account_id = serializers.IntegerField(required=True)
    to_account_id = serializers.IntegerField(required=True)
    currency = serializers.ChoiceField(Currency)

    class Meta:
        model = Transaction
        fields = ['id', 'comment', 'balance', 'currency', 'from_account_id', 'to_account_id', 'third_party_api',
                  'created_at', 'updated_at']

    def create(self, validated_data):
        try:
            validated_data["from_account"] = Account.objects.get(pk=validated_data['from_account_id'])
        except Account.DoesNotExist:
            raise serializers.ValidationError({"detail": "This transaction can't be created. "
                                              "The from_account not exist!"})

        try:
            validated_data["to_account"] = Account.objects.get(pk=validated_data['to_account_id'])
        except Account.DoesNotExist:
            raise serializers.ValidationError({"detail": "This transaction can't be created. "
                                              "The to_account not exist!"})

        del validated_data['from_account_id']
        del validated_data['to_account_id']
        try:
            return Transaction.objects.create(**validated_data)
        except ValueError:
            raise serializers.ValidationError({"detail": "This transaction can't be created. "
                                              "The from_account balance becomes negative!"})

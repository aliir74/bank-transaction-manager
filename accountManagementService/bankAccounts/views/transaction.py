from rest_framework import generics
from bankAccounts.models import Transaction
from bankAccounts.serializers.transaction import TransactionSerializer


class Transaction(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

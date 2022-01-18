from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from bankAccounts.models import Transaction
from bankAccounts.serializers.transaction import TransactionSerializer
from bankAccounts.authentication import Authentication


class Transaction(generics.CreateAPIView):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

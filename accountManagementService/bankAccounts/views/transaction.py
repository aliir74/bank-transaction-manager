from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from bankAccounts.models import Transaction as TransactionModel
from bankAccounts.serializers.transaction import TransactionSerializer
from bankAccounts.authentication import Authentication
from bankAccounts.api_docs.transaction import TransactionCreateRequest
from bankAccounts.api_docs import AuthenticationSchema


class Transaction(generics.CreateAPIView):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializer

    @swagger_auto_schema(manual_parameters=[AuthenticationSchema.auth_param],
                         request_body=TransactionCreateRequest.TRANSACTION_CREATE_REQUEST_SCHEMA,
                         responses=TransactionCreateRequest.TRANSACTION_CREATE_RESPONSE_SCHEMA)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

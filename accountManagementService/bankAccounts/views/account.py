from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from bankAccounts.models import Account
from bankAccounts.serializers.account import AccountSerializer
from bankAccounts.authentication import Authentication

from bankAccounts.api_docs.account import ACCOUNT_CREATE_REQUEST_SCHEMA, ACCOUNT_CREATE_RESPONSE_SCHEMA


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountList(mixins.CreateModelMixin, generics.ListAPIView):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @swagger_auto_schema(request_body=ACCOUNT_CREATE_REQUEST_SCHEMA, responses=ACCOUNT_CREATE_RESPONSE_SCHEMA)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

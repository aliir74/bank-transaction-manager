from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from bankAccounts.models import Account
from bankAccounts.serializers.account import AccountSerializer
from bankAccounts.authentication import Authentication


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

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

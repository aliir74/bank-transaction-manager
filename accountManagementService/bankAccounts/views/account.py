from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import get_object_or_404

from bankAccounts.models import Account, User
from bankAccounts.serializers.account import AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountList(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

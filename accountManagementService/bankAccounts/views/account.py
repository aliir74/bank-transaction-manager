from rest_framework import generics
from rest_framework import mixins
from bankAccounts.models import Account
from bankAccounts.serializers import AccountSerializer


class AccountView(mixins.CreateModelMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from bankAccounts.models import Account
from bankAccounts.serializers.account import AccountSerializer
from bankAccounts.authentication import Authentication

from bankAccounts.api_docs.account import AccountCreateRequest, AccountListRequest, \
    AccountGetRequest, AccountPutRequest, AccountPatchRequest, \
    AccountModelSchema


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @swagger_auto_schema(manual_parameters=[AccountModelSchema.id_param],
                         responses=AccountGetRequest.ACCOUNT_GET_RESPONSE_SCHEMA)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[AccountModelSchema.id_param],
                         request_body=AccountPutRequest.ACCOUNT_PUT_REQUEST_SCHEMA,
                         responses=AccountPutRequest.ACCOUNT_PUT_RESPONSE_SCHEMA)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[AccountModelSchema.id_param],
                         request_body=AccountPatchRequest.ACCOUNT_PATCH_REQUEST_SCHEMA,
                         responses=AccountPatchRequest.ACCOUNT_PATCH_RESPONSE_SCHEMA)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[AccountModelSchema.id_param])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AccountList(mixins.CreateModelMixin, generics.ListAPIView):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @swagger_auto_schema(request_body=AccountCreateRequest.ACCOUNT_CREATE_REQUEST_SCHEMA,
                         responses=AccountCreateRequest.ACCOUNT_CREATE_RESPONSE_SCHEMA)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @swagger_auto_schema(responses=AccountListRequest.ACCOUNT_LIST_RESPONSE_SCHEMA)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


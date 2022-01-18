from django.urls import path
from bankAccounts.views.account import AccountDetail, AccountList
from bankAccounts.views.transaction import Transaction

urlpatterns = [
    path('', AccountList.as_view(), name='account-list'),
    path('<int:pk>', AccountDetail.as_view(), name='account-details'),
    path('transaction', Transaction.as_view(), name='transaction')
]

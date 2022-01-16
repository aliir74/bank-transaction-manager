from django.urls import path
from bankAccounts.views.account import AccountDetail, AccountList

urlpatterns = [
    path('', AccountList.as_view()),
    path('<int:pk>', AccountDetail.as_view())
]

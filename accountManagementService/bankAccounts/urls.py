from django.urls import path
from bankAccounts.views.account import AccountView

urlpatterns = [
    path('', AccountView.as_view())
]

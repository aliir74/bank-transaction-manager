import decimal

from django.urls import reverse
from unittest.mock import patch, PropertyMock
from rest_framework.test import APITestCase
from django.conf import settings
from bankAccounts.models import Account, Transaction
from bankAccounts.models.base import Currency


class TransactionTests(APITestCase):
    def setUp(self) -> None:
        self.account_1 = Account.objects.create(id=1, currency=Currency.USD, balance=100, passport_id="1")
        self.account_2 = Account.objects.create(id=2, currency=Currency.USD, balance=100, passport_id="2")
        self.account_3 = Account.objects.create(id=3, currency=Currency.EUR, balance=100, passport_id="3")

    def test_same_currency_transaction_succeed(self):
        Transaction.objects.create(balance=50, currency=Currency.USD, from_account=self.account_1,
                                   to_account=self.account_2)
        self.account_1.refresh_from_db()
        self.account_2.refresh_from_db()

        self.assertEqual(self.account_1.balance, 50)
        self.assertEqual(self.account_2.balance, 150)

    @patch("currencyExchange.repositories.exchangeratesapiio.ExchangerRatesAPIIO.eur_to_usd", new_callable=PropertyMock)
    def test_different_currency_transaction_succeed(self, mock1):
        mock1.return_value = decimal.Decimal(0.3)
        Transaction.objects.create(balance=70, currency=Currency.EUR, from_account=self.account_1,
                                   to_account=self.account_2)
        self.account_1.refresh_from_db()
        self.account_2.refresh_from_db()

        self.assertEqual(self.account_1.balance, 100-0.3*70)
        self.assertEqual(self.account_2.balance, 100+0.3*70)

    def test_prevent_negative_balance(self):
        try:
            Transaction.objects.create(balance=5000, currency=Currency.USD, from_account=self.account_1,
                                   to_account=self.account_2)
        except Exception:
            self.assertRaises(ValueError)
        self.account_1.refresh_from_db()
        self.account_2.refresh_from_db()

        self.assertEqual(self.account_1.balance, 100)
        self.assertEqual(self.account_2.balance, 100)

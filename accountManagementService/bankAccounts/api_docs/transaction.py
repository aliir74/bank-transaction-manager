from drf_yasg.openapi import Schema, TYPE_STRING, TYPE_NUMBER, TYPE_ARRAY, TYPE_INTEGER, TYPE_OBJECT
from rest_framework import status


class TransactionModelSchema:
    schema = Schema(
        type=TYPE_OBJECT,
        properties={
            'id': Schema(
                type=TYPE_INTEGER,
                title="Created Transaction's Id",
            ),
            'balance': Schema(
                type=TYPE_NUMBER,
                title='Balance',
            ),
            'currency': Schema(
                type=TYPE_STRING,
                title="Transaction Currency",
                description="There is two choice: USD, EUR."
            ),
            'to_account_id': Schema(
                type=TYPE_INTEGER,
                title="Money Transfer To Account",
                description="Money transfer to the account with this id."
            ),
            'from_account_id': Schema(
                type=TYPE_INTEGER,
                title="Money Transfer From Account",
                description="Money transfer from the account with this id."
            ),
            'comment': Schema(
                type=TYPE_STRING,
                title="Transaction's Comment"
            ),
            'third_party_api': Schema(
                type=TYPE_STRING,
                title="The Currency Exchanger Third Party",
                description="If the currency of transaction and account isn't equal, we must get exchange rate from"
                            " third party api. Now there is only one third party: 'exchangeratesapi.io'."
            ),
            'created_at': Schema(
                type=TYPE_STRING,
                title="Transaction Creation Time"
            ),
            'updated_at': Schema(
                type=TYPE_STRING,
                title='Last Update Time of The Transaction'
            )
        }
    )


class TransactionCreateRequest:
    TRANSACTION_CREATE_REQUEST_SCHEMA = Schema(
        type=TYPE_OBJECT,
        properties={
            'balance': Schema(
                type=TYPE_NUMBER,
                title='Balance',
            ),
            'currency': Schema(
                type=TYPE_STRING,
                title="Transaction Currency",
                description="There is two choice: USD, EUR. the default is USD."
            ),
            'to_account_id': Schema(
                type=TYPE_INTEGER,
                title="Money Transfer To Account",
                description="Money transfer to the account with this id."
            ),
            'from_account_id': Schema(
                type=TYPE_INTEGER,
                title="Money Transfer From Account",
                description="Money transfer from the account with this id."
            ),
            'comment': Schema(
                type=TYPE_STRING,
                title="Transaction's Comment"
            ),
            'third_party_api': Schema(
                type=TYPE_STRING,
                title="The Currency Exchanger Third Party",
                description="If the currency of transaction and account isn't equal, we must get exchange rate from"
                            " third party api. Now there is only one third party: 'exchangeratesapi.io'."
            ),
        },
        required=['balance', 'currency', 'to_account_id', 'from_account_id']
    )

    TRANSACTION_CREATE_RESPONSE_SCHEMA = {
        status.HTTP_201_CREATED: TransactionModelSchema.schema
    }
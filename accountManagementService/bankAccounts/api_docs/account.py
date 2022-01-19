from drf_yasg.openapi import Schema, TYPE_STRING, TYPE_NUMBER, TYPE_ARRAY, TYPE_INTEGER, TYPE_OBJECT
from rest_framework import status

ACCOUNT_CREATE_REQUEST_SCHEMA = Schema(
    type=TYPE_OBJECT,
    properties={
        'balance': Schema(
            type=TYPE_NUMBER,
            title='Base Balance',
            description='The base balance of your new bank account.'
        ),
        'passport_id': Schema(
            type=TYPE_STRING,
            title="Owner's Passport Id",
            description=''
        ),
        'currency': Schema(
            type=TYPE_STRING,
            title="Balance Account Currency",
            description="There is two choice: USD, EUR.\n The default is USD."
        )
    },
    required=['balance', 'passport_id']
)

ACCOUNT_CREATE_RESPONSE_SCHEMA = {
    status.HTTP_201_CREATED: Schema(
        type=TYPE_ARRAY,
        items=Schema(
            type=TYPE_OBJECT,
            properties={
                'id': Schema(
                    type=TYPE_INTEGER,
                    title="Created Account's Id",
                    description="You should use this id to perform further actions on this account."
                ),
                'balance': Schema(
                    type=TYPE_NUMBER,
                    title='Base Balance',
                    description='The base balance of your new bank account.'
                ),
                'passport_id': Schema(
                    type=TYPE_STRING,
                    title="Owner's Passport Id",
                    description=''
                ),
                'currency': Schema(
                    type=TYPE_STRING,
                    title="Balance Account Currency",
                    description="There is two choice: USD, EUR."
                ),
                'created_at': Schema(
                    type=TYPE_STRING,
                    title="Account Creation Time"
                ),
                'updated_at': Schema(
                    type=TYPE_STRING,
                    title='Last Update Time of The Account'
                )
            },
        )
    )
}


ACCOUNT_LIST_REQUEST_SCHEMA = {
    status.HTTP_200_OK: Schema(
        type=TYPE_OBJECT,
        properties={
            'balance': Schema(
                type=TYPE_NUMBER,
                title='Base Balance',
                description='The base balance of your new bank account.'
            ),
            'passport_id': Schema(
                type=TYPE_STRING,
                title="Owner's Passport Id",
                description=''
            ),
            'currency': Schema(
                type=TYPE_STRING,
                title="Balance Account Currency",
                description="There is two choice: USD, EUR.\n The default is USD."
            )
        },
        required=['balance', 'passport_id']
    )
}

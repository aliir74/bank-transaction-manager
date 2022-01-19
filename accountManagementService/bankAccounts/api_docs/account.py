from drf_yasg.openapi import Schema, Parameter, IN_PATH, \
    TYPE_STRING, TYPE_NUMBER, TYPE_ARRAY, TYPE_INTEGER, TYPE_OBJECT
from rest_framework import status


class AccountModelSchema:
    schema = Schema(
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
        }
    )

    id_param = Parameter('id', IN_PATH, description="Account's Id", type=TYPE_INTEGER)


class AccountCreateRequest:
    ACCOUNT_CREATE_REQUEST_SCHEMA = Schema(
        type=TYPE_OBJECT,
        properties={
            'balance': Schema(
                type=TYPE_NUMBER,
                title='Base Balance',
                description='The base balance of the new bank account.'
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
        status.HTTP_201_CREATED: AccountModelSchema.schema
    }


class AccountGetRequest:
    ACCOUNT_GET_RESPONSE_SCHEMA = {
        status.HTTP_200_OK: AccountModelSchema.schema
    }


class AccountPutRequest:
    ACCOUNT_PUT_RESPONSE_SCHEMA = {
        status.HTTP_200_OK: AccountModelSchema.schema
    }
    ACCOUNT_PUT_REQUEST_SCHEMA = AccountCreateRequest.ACCOUNT_CREATE_REQUEST_SCHEMA


class AccountPatchRequest:
    ACCOUNT_PATCH_RESPONSE_SCHEMA = {
        status.HTTP_200_OK: AccountModelSchema.schema
    }
    ACCOUNT_PATCH_REQUEST_SCHEMA = Schema(
        type=TYPE_OBJECT,
        properties={
            'balance': Schema(
                type=TYPE_NUMBER,
                title='Base Balance',
                description='The base balance of the bank account.'
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
        }
    )


class AccountListRequest:
    ACCOUNT_LIST_RESPONSE_SCHEMA = {
        status.HTTP_200_OK: Schema(
            type=TYPE_ARRAY,
            items=AccountModelSchema.schema
        )
    }

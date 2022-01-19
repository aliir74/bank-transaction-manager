from drf_yasg.openapi import Parameter, IN_HEADER, TYPE_STRING


class AuthenticationSchema:
    auth_param = Parameter('AUTHORIZATION', IN_HEADER, description="You must put your token in this header.", type=TYPE_STRING)
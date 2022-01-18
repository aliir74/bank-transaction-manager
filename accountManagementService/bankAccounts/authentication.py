from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth.models import AnonymousUser


class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return None

        if token != settings.SERVICE_AUTH_TOKEN:
            raise exceptions.AuthenticationFailed('No such user')

        return AnonymousUser, None


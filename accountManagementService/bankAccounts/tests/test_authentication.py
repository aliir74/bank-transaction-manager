from django.urls import reverse
from rest_framework.test import APITestCase
from django.conf import settings


class AccountTests(APITestCase):
    def setUp(self) -> None:
        self.auth_header = {'HTTP_AUTHORIZATION': settings.SERVICE_AUTH_TOKEN}

    def test_authentication_failed_with_wrong_token(self):
        status_codes = []
        url = reverse('account-list')
        status_codes.append(self.client.get(url).status_code)
        status_codes.append(self.client.post(url).status_code)

        url = reverse('account-details', kwargs={'pk': 1})
        status_codes.append(self.client.get(url).status_code)
        status_codes.append(self.client.patch(url).status_code)
        status_codes.append(self.client.put(url).status_code)
        status_codes.append(self.client.delete(url).status_code)

        url = reverse('transaction')
        status_codes.append(self.client.post(url).status_code)

        self.assertListEqual(status_codes, [403]*len(status_codes))

    def test_authentication_succeed(self):
        status_codes = []
        url = reverse('account-list')
        status_codes.append(self.client.get(url, **self.auth_header).status_code)
        status_codes.append(self.client.post(url, **self.auth_header).status_code)

        url = reverse('account-details', kwargs={'pk': 1})
        status_codes.append(self.client.get(url, **self.auth_header).status_code)
        status_codes.append(self.client.patch(url, **self.auth_header).status_code)
        status_codes.append(self.client.put(url, **self.auth_header).status_code)
        status_codes.append(self.client.delete(url, **self.auth_header).status_code)

        url = reverse('transaction')
        status_codes.append(self.client.post(url, **self.auth_header).status_code)

        for code in status_codes:
            self.assertNotEqual(code, 403)


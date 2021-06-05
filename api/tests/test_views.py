from oauth2_provider.settings import oauth2_settings
from oauth2_provider.models import get_access_token_model, get_application_model
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APITestCase
from api.models import Country, State, Address
from django.urls import reverse
from mixer.backend.django import mixer

Application = get_application_model()
AccessToken = get_access_token_model()
UserModel = get_user_model()
import pytest

@pytest.mark.django_db
class Test_mytest(APITestCase):
    def setUp(self):
        oauth2_settings._SCOPES = ["read", "write", "scope1", "scope2", "resource1"]
        self.test_user = UserModel.objects.create_user("test_user", "test@example.com", "123456")
        self.application = Application.objects.create(
                                                name="Test Application",
                                                redirect_uris="http://localhost http://example.com http://example.org",
                                                user=self.test_user,
                                                client_type=Application.CLIENT_CONFIDENTIAL,
                                                authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
                                            )

        self.access_token = AccessToken.objects.create(
                                                    user=self.test_user,
                                                    scope="read write",
                                                    expires=timezone.now() + timezone.timedelta(seconds=300),
                                                    token="secret-access-token-key",
                                                    application=self.application
                                                )

        self.access_token.scope = "read"
        self.access_token.save()
        self.auth = "Bearer {0}".format(self.access_token.token)


    def test_countrylist(self):
        path = reverse('countrylist')
        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        assert response.status_code == 200

    def test_country_filter_By_Code(self):
        path = reverse('country', kwargs={'filter': 'BD'})
        country = mixer.blend(Country, Code='BD')
        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        assert response.status_code == 200

    def test_country_filter_By_Name(self):
        path = reverse('country', kwargs={'filter': 'Bangladesh'})
        country = mixer.blend(Country, Name='Bangladesh')
        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        assert response.status_code == 200

    def test_statelist(self):
        path = reverse('statelist')
        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        assert response.status_code == 200

    def test_state_filter(self):
        path = reverse('state', kwargs={'st': 'state1'})
        country = mixer.blend(State, Name='state1')
        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        assert response.status_code == 200

    def test_addresslist(self):
        path = reverse('addresslist')
        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        assert response.status_code == 200

    def test_address_By_RoadNumber(self):
        path = reverse('address_rn', kwargs={'rn': 123})
        country = mixer.blend(Address, Road_number=123)
        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        assert response.status_code == 200

    def test_address_By_HouseNumber(self):
        path = reverse('address_hn', kwargs={'hn': '13c4'})
        country = mixer.blend(Address, House_number='13c4')
        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        assert response.status_code == 200

    def test_address_Details(self):
        path = reverse('address_details', kwargs={'pk': 1})
        country = mixer.blend(Address)
        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        assert response.status_code == 200
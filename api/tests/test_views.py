from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from api.models import Country, State, Address
import pytest

@pytest.mark.django_db
class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_countrylist(self):
        path = reverse('countrylist')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_country_filter_By_Code(self):
        path = reverse('country', kwargs={'filter': 'BD'})
        country = mixer.blend(Country, Code='BD')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_country_filter_By_Name(self):
        path = reverse('country', kwargs={'filter': 'Bangladesh'})
        country = mixer.blend(Country, Name='Bangladesh')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_statelist(self):
        path = reverse('statelist')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_state_filter(self):
        path = reverse('state', kwargs={'st': 'state1'})
        country = mixer.blend(State, Name='state1')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_addresslist(self):
        path = reverse('addresslist')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_address_By_RoadNumber(self):
        path = reverse('address_rn', kwargs={'rn': 123})
        country = mixer.blend(Address, Road_number=123)
        response = self.client.get(path)
        assert response.status_code == 200

    def test_address_By_HouseNumber(self):
        path = reverse('address_hn', kwargs={'hn': '13c4'})
        country = mixer.blend(Address, House_number='13c4')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_address_Details(self):
        path = reverse('address_details', kwargs={'pk': 1})
        country = mixer.blend(Address)
        response = self.client.get(path)
        assert response.status_code == 200
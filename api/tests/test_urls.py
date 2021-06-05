from django.urls import resolve, reverse

class TestUrls:
    def test_countrylist_url(self):
        path = reverse('countrylist')
        assert resolve(path).view_name == 'countrylist'

    def test_country_url(self):
        path = reverse('country', kwargs={'filter': 'BD'})
        assert resolve(path).view_name == 'country'

    def test_statelist_url(self):
        path = reverse('statelist')
        assert resolve(path).view_name == 'statelist'

    def test_state_url(self):
        path = reverse('state', kwargs={'st': 'st1'})
        assert resolve(path).view_name == 'state'

    def test_addresslist_url(self):
        path = reverse('addresslist')
        assert resolve(path).view_name == 'addresslist'

    def test_address_rn_url(self):
        path = reverse('address_rn', kwargs={'rn': 123})
        assert resolve(path).view_name == 'address_rn'

    def test_address_hn_url(self):
        path = reverse('address_hn', kwargs={'hn': 'hn1'})
        assert resolve(path).view_name == 'address_hn'

    def test_addressDetails_url(self):
        path = reverse('address_details', kwargs={'pk': 1})
        assert resolve(path).view_name == 'address_details'
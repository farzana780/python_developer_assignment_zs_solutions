from rest_framework import serializers
from .models import Country, State, Address


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['Name']


class CountryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['Name', 'Latitude', 'Longitude', 'Code']


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['Name']


class StateByCountrySerialzer(serializers.ModelSerializer):
    state = StateSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['Name', 'state']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['Name', 'House_number', 'Road_number', 'state']


class AddressOfStatesSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True, read_only=True)
    class Meta:
        model = State
        fields = ['Name', 'address']


class AddressDetailsSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source='state.Name', read_only=True)
    country = serializers.CharField(source='state.country', read_only=True)
    class Meta:
        model = Address
        fields = ['Name', 'House_number', 'Road_number', 'state', 'country']



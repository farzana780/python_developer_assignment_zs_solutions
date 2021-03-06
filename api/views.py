from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Country, State, Address
from api.serializers import CountrySerializer, AddressSerializer, CountryDetailsSerializer, \
    StateByCountrySerialzer, AddressOfStatesSerializer, AddressDetailsSerializer
from rest_framework.permissions import IsAuthenticated
import requests
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user = authenticate(username=request.data['username'], password=request.data['password'])
    if user:
        r = requests.post(
            'http://127.0.0.1:8000/o/token/',
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': request.data['client_id'],
                'client_secret': request.data['client_secret'],
            },
        )
        return Response(r.json())
    else:
        message = {
            'status': 'wrong username & password'
        }
        return JsonResponse(message)


class Countrylist(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, filter=None, format=None):
        if filter is not None:
            try:
                country = Country.objects.get(Name = filter)
            except Country.DoesNotExist:
                country = Country.objects.get(Code = filter)
            country_serializer = CountryDetailsSerializer(country)
            return Response(country_serializer.data)
        country = Country.objects.all()
        country_serializer = CountrySerializer(country, many=True)
        return Response(country_serializer.data)



class Statelist(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, st=None, format=None):
        statebycountry = Country.objects.all()
        if st is not None:
            state = State.objects.all()
            s = get_object_or_404(state, Name=st)
            statebycountry = state.filter(Name=s)
        state_serializer = StateByCountrySerialzer(statebycountry, many=True)
        return Response(state_serializer.data)


class Addresslist(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, rn=None, hn=None, format=None):
        addressbystate = State.objects.all()
        address_serializer = AddressOfStatesSerializer(addressbystate, many=True)
        if rn is not None:
            address = Address.objects.all()
            a = get_object_or_404(address, Road_number=rn)
            addressbystate = address.filter(Road_number=a.Road_number)
            address_serializer = AddressSerializer(addressbystate, many=True)
        if hn is not None:
            address = Address.objects.all()
            a = get_object_or_404(address, House_number=hn)
            addressbystate = address.filter(House_number=a.House_number)
            address_serializer = AddressSerializer(addressbystate, many=True)
        return Response(address_serializer.data)


class AddressDetailslist(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, format=None):
        address = Address.objects.get(id=pk)
        address_serializer = AddressDetailsSerializer(address)
        return Response(address_serializer.data)



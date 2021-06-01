"""python_developer_assignment_zs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('country/', views.Countrylist.as_view(), name='countrylist'),
    path('country-filter/<str:filter>', views.Countrylist.as_view(), name='country'),
    path('state/', views.Statelist.as_view(), name='statelist'),
    path('state-filter/<str:st>', views.Statelist.as_view(), name='state'),
    path('address/', views.Addresslist.as_view(), name='addresslist'),
    path('address-filter/<int:rn>', views.Addresslist.as_view(), name='address'),
    path('address-filter/<str:hn>', views.Addresslist.as_view(), name='address'),
    path('address-details/<int:pk>', views.AddressDetailslist.as_view(), name='address'),
]

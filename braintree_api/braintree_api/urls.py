"""braintree_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from api import views
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewset,
                base_name='customer')
router.register('customers/(?P<customer_id>[a-z0-9]+)/payment-methods',
                views.CustomerPaymentMethodViewset,
                base_name='customer-payment-method')
router.register('customers/(?P<customer_id>[a-z0-9]+)/transactions',
                views.CustomerTransactionViewset,
                base_name='customer-transaction')
router.register('payment-methods',
                views.PaymentMethodViewset,
                base_name='payment-method')
router.register('transactions',
                views.TransactionViewset,
                base_name='transaction')


urlpatterns = [
    url(
        r'^customers/(?P<customer_id>[a-z0-9]+)/payment-method-form',
        views.PaymentMethodFormView.as_view(),
        name='customer-payment-method-form'
    ),
    url(
        r'^settings',
        views.BraintreeSettingsView.as_view(),
        name='braintree-settings'
    ),
    url(r'^', include(router.urls)),
]

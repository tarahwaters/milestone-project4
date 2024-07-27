from django.urls import path
from .views import bespoke_enquiry, bespoke_success

urlpatterns = [
    path('', bespoke_enquiry, name='bespoke_enquiry'),
    path('bespoke_success/', bespoke_success, name='bespoke_success'),
]

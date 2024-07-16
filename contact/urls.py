from django.urls import path
from .views import faq_list

urlpatterns = [
    path('', views.contact, name='contact'),
]

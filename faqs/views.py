from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all()
    return(request, 'faqs/faq_list.html', {'faqs': faqs})



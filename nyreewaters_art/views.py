from django.shortcuts import render
from django.http import HttpResponseServerError

def trigger_500_view(request):
    """ View used to test the Custom 500 Server Error page """
    return HttpResponseServerError(render(request, '500.html'))
from django.shortcuts import render
from django.http import Http404

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

def trigger_404(request):
    raise Http404("This is a test 404 error")

def trigger_500(request):
    1 / 0
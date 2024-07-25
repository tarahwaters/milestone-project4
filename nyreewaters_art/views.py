from django.shortcuts import render


def custom_403(request, exception):
    """ Error Handler 403 """
    return render(request, '403.html', status=404)

def custom_404(request, exception):
    """ Error Handler 404 """
    return render(request, '404.html', status=404)

def custom_500(request):
    """ Error Handler 500 """
    return render(request, '500.html', status=500)
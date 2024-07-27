from django.shortcuts import render, redirect
from .forms import BespokeForm


def bespoke_enquiry(request):
    if request.method == 'POST':
        form = BespokeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bespoke_success')
    else:
        form = BespokeForm()
    return render(request, 'bespoke/bespoke_enquiry.html', {'form': form})


def bespoke_success(request):
    return render(request, 'bespoke/bespoke_success.html')

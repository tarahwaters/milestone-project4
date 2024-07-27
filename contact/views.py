from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """ Return the contact form page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                    request, 'Your message was sent successfully - thank you!')
            return redirect('contact')
        else:
            messages.error(
                request, 'There was an error submitting the form. \
                Please make sure the information is valid.')
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)

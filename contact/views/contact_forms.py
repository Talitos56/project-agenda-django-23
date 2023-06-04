
from django.shortcuts import render

from contact import forms


def create(request):
    if request.method == 'POST':
        context = {
            'form': forms.ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'forms': forms.ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context,
    )

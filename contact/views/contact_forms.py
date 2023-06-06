
from django.shortcuts import redirect, render

from contact import forms


def create(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

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

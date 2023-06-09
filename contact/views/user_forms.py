from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact import forms
from contact.forms import RegisterForm


def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

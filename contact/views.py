# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail

from .forms import ContactForm

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            send_mail(
							contact_name, 
							form_content, 
							contact_email, 
							['henryco4388@gmail.com'], 
							fail_silently=False
							)

            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })
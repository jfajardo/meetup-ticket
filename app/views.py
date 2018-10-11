import requests
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, TextInput
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import Ticket


API_KEY = '233839657c671121404d4a7e374a28c'
URL_GROUP = 'Python-Pasto'
EVENT_ID = '253612928'


def index(request):
    try:
        if request.user.is_authenticated:
            if not Ticket.objects.filter(user=request.user).exists():
                url = 'https://api.meetup.com/{0}/events/{1}/attendance?key={2}&only=member.id'.format(URL_GROUP, EVENT_ID, API_KEY)
                response = requests.get(url)
                uid = request.user.social_auth.get(provider='meetup').uid
                register = False
                if uid in str(response.json()):
                    register = True
                    ticket, created = Ticket.objects.get_or_create(user=request.user)
                    return render(request, 'dashboard.html', {
                        'register': str(register.id),
                        'ticket': ticket,
                    })
                return render(request, 'dashboard.html', {'register': register})
            else:
                return render(request, 'dashboard.html', {
                    'register': True,
                    'ticket': Ticket.objects.get(user=request.user),
                })
        return render(request, 'index.html', {})
    except Exception as ex:
        print(ex)
        return render(request, 'index.html', {})


def logout_view(request):
    logout(request)
    return redirect('/')


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': TextInput(attrs={'class': 'form-control', 'required': 'required', 'type':'email'}),
        }
        labels = {
            'first_name': _('Nombre'),
            'last_name': _('Apellido'),
            'email': _('Email'),
        }


class UserEditView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, '😁 Información Actualizada!')
        return reverse_lazy('index')

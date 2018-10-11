from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('me', UserEditView.as_view(), name='me'),
    path('logout', logout_view, name='logout')
]

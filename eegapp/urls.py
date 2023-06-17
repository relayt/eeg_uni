from django.urls import path
from eegapp.views import main

app_name = 'eegapp'

urlpatterns = [
    path('', main, name = 'application'),
]
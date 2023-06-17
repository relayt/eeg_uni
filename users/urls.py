from django.urls import path
from users.views import authorization

app_name = 'users'

urlpatterns = [
    path('', authorization, name='authorization'),
]
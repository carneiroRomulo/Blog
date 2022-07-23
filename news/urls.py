
from django.urls import path

from .views import home

app_name = 'backend'

urlpatterns = [
    path('', home, name='home'),
]

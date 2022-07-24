
from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.home, name='search'),
    path(
        'category/<str:category_name>/',
        views.home,
        name="category"
    ),
]

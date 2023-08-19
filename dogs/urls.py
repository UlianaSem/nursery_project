from dogs.apps import DogsConfig
from django.urls import path

from dogs.views import home


app_name = DogsConfig.name

urlpatterns = [
    path('', home, name='home'),
]

from dogs.apps import DogsConfig
from django.urls import path

from dogs.views import home, breeds, breed_dogs


app_name = DogsConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('breeds/', breeds, name='breeds'),
    path('<int:pk>/breeds/', breed_dogs, name='breed_dogs'),
]

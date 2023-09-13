from django.views.decorators.cache import cache_page

from dogs.apps import DogsConfig
from django.urls import path

from dogs.views import IndexView, BreedListView, DogListView, DogCreateView, DogUpdateView, DogDeleteView


app_name = DogsConfig.name

urlpatterns = [
    path('', cache_page(60)(IndexView.as_view()), name='home'),
    path('breeds/', BreedListView.as_view(), name='breeds'),
    path('<int:pk>/breeds/', DogListView.as_view(), name='breed_dogs'),
    path('create/dog/', DogCreateView.as_view(), name='create_dog'),
    path('<int:pk>/update/dog/', DogUpdateView.as_view(), name='update_dogs'),
    path('<int:pk>/delete/dog/', DogDeleteView.as_view(), name='delete_dogs'),
]

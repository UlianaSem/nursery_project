from django.shortcuts import render
from dogs.models import Breed


# Create your views here.
def home(request):
    context = {
        'object_list': Breed.objects.all()[:3],
        'title': 'Главная'
    }
    return render(request, 'dogs/index.html', context)


def breeds(request):
    context = {
        'object_list': Breed.objects.all(),
        'title': 'Наши породы'
    }
    return render(request, 'dogs/breeds.html', context)


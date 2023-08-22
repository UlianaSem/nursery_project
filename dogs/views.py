from django.shortcuts import render
from dogs.models import Breed, Dog


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


def breed_dogs(request, pk):
    breed = Breed.objects.get(pk=pk)

    context = {
        'object_list': Dog.objects.filter(breed_id=pk),
        'title': f'Собаки породы {breed.breed_name}'
    }
    return render(request, 'dogs/dogs.html', context)

from django.contrib import admin

from dogs.models import Dog, Breed, Parent


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dog_name', 'breed_id', 'birthday']
    list_filter = ['breed_id']


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['pk', 'breed_name', 'description']


@admin.register(Parent)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dog_name', 'breed_id', 'birthday', 'dog']

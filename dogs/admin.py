from django.contrib import admin

from dogs.models import Dog, Breed


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['dog_name', 'breed_id', 'birthday']
    list_filter = ['breed_id']


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['breed_name', 'description']

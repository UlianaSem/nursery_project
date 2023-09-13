from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy, reverse

from dogs.forms import DogForm, ParentForm
from dogs.models import Breed, Dog, Parent
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from dogs.services import get_breeds_cache


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dogs/index.html'
    extra_context = {
        'title': 'Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Breed.objects.all()[:3]
        return context_data


class BreedListView(LoginRequiredMixin, ListView):
    model = Breed

    extra_context = {
        'title': 'Наши породы'
    }

    def get_queryset(self):
        return get_breeds_cache()


class DogListView(LoginRequiredMixin, ListView):
    model = Dog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(breed_id=self.kwargs.get('pk'))

        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        breed_item = Breed.objects.get(pk=self.kwargs.get('pk'))
        context_data['breed_pk'] = breed_item.pk
        context_data['title'] = f'Собаки породы {breed_item.breed_name}'

        return context_data


class DogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Dog
    form_class = DogForm
    permission_required = 'dogs.add_dog'
    success_url = reverse_lazy('dogs:breeds')
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        
        return super().form_valid(form)


class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    form_class = DogForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404

        return self.object

    def get_success_url(self):
        print([self.object.breed_id])
        return reverse('dogs:breed_dogs', args=[self.object.breed_id.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Dog, Parent, form=ParentForm, extra=1)

        if self.request.method == "POST":
            formset = ParentFormset(self.request.POST, instance=self.object)
        else:
            formset = ParentFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class DogDeleteView(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs:breeds')

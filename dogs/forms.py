import datetime

from django import forms

from dogs.models import Dog, Parent


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DogForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Dog
        exclude = ('owner', )

    def clean_birthday(self):
        cleaned_data = self.cleaned_data['birthday']
        now_year = datetime.datetime.now().year

        if now_year - cleaned_data.year > 100:
            raise forms.ValidationError('Собака должна быть моложе ста лет')

        return cleaned_data


class ParentForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Parent
        fields = "__all__"

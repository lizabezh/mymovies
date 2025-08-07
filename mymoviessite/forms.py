from django.contrib.auth.forms import UserCreationForm

from .models import movies, Users
from django.forms import ModelForm, TextInput, NumberInput, Textarea

class MoviesForm(ModelForm):
    class Meta:
        model = movies
        fields = ['title', 'description', 'year', 'movie_url']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Movie title'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Movie description'
            }),
            "year": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Year of release'
            }),
            "movie_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Movie url'
            }),
        }

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ['username', 'email', 'password1', 'password2']

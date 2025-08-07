import form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, FormView, CreateView

from .forms import MoviesForm, RegisterForm
from .models import Users, movies


def index(request):
    return render(request, 'mymoviessite/index.html')


def search(request):
    return render(request, 'mymoviessite/search.html')


@login_required
def profile(request):
    return render(request, 'mymoviessite/profile.html')


def movies(request):
    movies = movies.objects.order_by('-created_at')
    return render(request, 'mymoviessite/movies.html', {'movies': movies})


class MovieDetailView(DetailView):
    model = movies
    template_name = 'mymoviessite/details_view.html'
    context_object_name = 'movie'


class MovieUpdateView(UpdateView):
    model = movies
    template_name = 'mymoviessite/add_movie.html'
    form_class = MoviesForm


class MovieDeleteView(DeleteView):
    model = movies
    success_url = '/movies'
    template_name = 'mymoviessite/movie_delete.html'


class RegisterView(CreateView):
    model = Users
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        # Переопределение метода form_valid для выполнения дополнительных действий
        response = super().form_valid(form)
        # Дополнительные действия (если нужно)
        return response


def change_password(request):
    if request.method == 'POST':
        user = Users.objects.get(username=request.user.username)
        new_password = request.POST.get('new_password')
        user.set_password(new_password)
        user.save()
        return redirect('profile')  # Перенаправление на страницу профиля или другую страницу

    return render(request, 'register.html')


def add_movie(request):
    error = ''
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Mistakes in format'

    form = MoviesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mymoviessite/add_movie.html', data)

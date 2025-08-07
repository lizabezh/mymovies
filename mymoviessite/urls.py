from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.search, name='search'),
    path('profile', views.profile, name='profile'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('movies/<int:pk>', views.MovieDetailView.as_view(), name='details_view'),
    path('movies/<int:pk>/update', views.MovieUpdateView.as_view(), name='movie_update'),
    path('movies', views.movies, name='movies'),
    path('add_movie', views.add_movie, name='add_movie'),
    path('movies/<int:pk>/delete', views.MovieDeleteView.as_view(), name='movie_delete')
]
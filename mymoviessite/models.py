from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie_url = models.TextField()

    def __str__(self):
        return f'Movie: {self.title}'

    def get_absolute_url(self):
        return f'/movies/{self.movie_id}'

    class Meta:
        db_table = 'movies'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Users(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='mymoviessite_users',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    # Добавьте related_name для обратной связи с разрешениями пользователей
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='mymoviessite_users',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )


class MovieViewers(models.Model):
    viewer_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    avatar = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'movie_viewers'


class Actors(models.Model):
    actor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'actors'


class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'countries'


class Genres(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'genres'


class MovieActors(models.Model):
    id = models.AutoField(primary_key=True)
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(movies, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'movie_actors'


class MovieCountries(models.Model):
    id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(movies, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'movie_countries'


class MovieGenres(models.Model):
    id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(movies, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'movie_genres'


class MovieImages(models.Model):
    id = models.AutoField(primary_key=True)
    image_data = models.BinaryField()
    movie_id = models.ForeignKey(movies, on_delete=models.CASCADE)
    ord = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'movie_images'


class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(movies, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'ratings'

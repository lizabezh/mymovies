from django.contrib import admin
from .models import Actors
from .models import (movies, Users)
from .models import (MovieActors, MovieGenres, MovieImages, MovieViewers, MovieCountries, Genres,
                     Ratings, Countries)

admin.site.register(Actors)
admin.site.register(MovieActors)
admin.site.register(MovieGenres)
admin.site.register(MovieImages)
admin.site.register(MovieViewers)
admin.site.register(Genres)
admin.site.register(Countries)
admin.site.register(Ratings)
admin.site.register(movies)
admin.site.register(Users)
admin.site.register(MovieCountries)
# Register your models here.

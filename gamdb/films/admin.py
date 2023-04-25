from django.contrib import admin

from .models import Movie, Director, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'director', 'genres_display'] #defines what is seen in the overall table
    list_display_links = ['name'] #what is link
    search_fields = ['name']
    list_filter = ['genres', 'year']

admin.site.register(Movie, MovieAdmin)
from django.contrib import admin

from .models import Movie, Director, Genre, Actor, Comment

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'director', 'genres_display']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['genres', 'year']

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Comment)
admin.site.register(Movie, MovieAdmin)
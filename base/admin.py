from django.contrib import admin
from .models import User, Director, Actor, Genre, Review, Writer, Movie, WatchList
# Register your models here.

admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Writer)
admin.site.register(Movie)
admin.site.register(WatchList)

from django.contrib import admin

from .models import Movie, Participant, Language, Genre

admin.site.register(Movie)
admin.site.register(Participant)
admin.site.register(Genre)
admin.site.register(Language)
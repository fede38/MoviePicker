from django.db import models


class Participant(models.Model):
    full_name = models.CharField(unique=True, primary_key=True, max_length=128)

    def __str__(self):
        return self.full_name


class Genre(models.Model):
    name = models.CharField(unique=True, primary_key=True, max_length=64)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=64)
    reduced_name = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Movie(models.Model):
    original_title = models.CharField(max_length=64)
    spanish_title = models.CharField(blank=True, max_length=64)
    english_title = models.CharField(blank=True, max_length=64)
    plot = models.TextField(default="")
    poster = models.ImageField(blank=True, upload_to="images")
    imdb_rating = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    rotten_rating = models.IntegerField(default=0)
    watched = models.BooleanField(default=False)
    year_of_release = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    actors = models.ManyToManyField(Participant)
    director = models.ForeignKey(Participant, null=True, on_delete=models.SET_NULL, related_name="director")
    # TODO buscar manera de agregar videos para guardar el trailer
    # TODO agregar nuestro propio rating
    # TODO parental rating

    def __str__(self):
        return self.original_title

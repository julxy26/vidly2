""" import models onto admin page"""
from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    """ list all fields we want to display """
    list_display = ("id", "name")


class MovieAdmin(admin.ModelAdmin):
    """ list all fields we want exclude """
    exclude = ("date_created", )
    # or fields =
    list_display = ("title", "number_in_stock", "daily_rate")


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

from django.urls import path
from . import views

""" define app name => no need to specify in name """
app_name = "movies"

# url configuration
urlpatterns = [
    path("", views.index, name="index"),
    # int: => only integers can be passed in the params
    path("<int:movie_id>", views.detail, name="detail")
]

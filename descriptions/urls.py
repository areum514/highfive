from django.urls import path
from . import views


app_name = "descriptions"
urlpatterns = [
    path("/", views.home_page, name="home"),
]

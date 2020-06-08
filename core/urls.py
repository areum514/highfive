from django.urls import path
from descriptions import views as descriptions_views

app_name = "core"
urlpatterns = [
    path("", descriptions_views.home_page, name="home"),
]

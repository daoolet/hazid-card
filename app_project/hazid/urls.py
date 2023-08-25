from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_hazid, name="create_hazid"),
    path("<int:survey_id>", views.read_hazid, name="read_hazid"),
]
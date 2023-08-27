from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("read/<int:survey_id>/", views.read_survey, name="read_survey"),
    path("create/", views.create_survey, name="create_survey"),
]
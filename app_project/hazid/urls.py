from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("read/<int:survey_id>/", views.read_survey, name="read_survey"),
    path("create/", views.create_survey, name="create_survey"),
    path("stats/", views.stats, name="stats"),
    path("winners/", views.winners, name="winners"),
    path("qr/", views.qr, name="qr"),
]
from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="polls-index"),
    path("owner/", views.polls_main, name="owner"),
    path("<int:question_id>/", views.detail, name="details"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

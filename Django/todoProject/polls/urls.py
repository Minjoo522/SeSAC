from django.urls import path
from . import views

urlpatterns = [
    path("", views.polls_list, name="polls_list"),
    path("<int:question_id>/", views.polls_choice, name="polls_choice"),
    path("<int:question_id>/<int:choice_id>/result", views.polls_result, name="polls_result"),
]
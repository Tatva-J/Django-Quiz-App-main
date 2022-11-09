from django.urls import path
from .views import *

urlpatterns = [
    path("index-menu/", index_page, name="index_page"),
    path("start-quiz/", take_quiz, name="start_quiz"),
    path("before-quiz/", before_quiz, name="before_quiz"),
]

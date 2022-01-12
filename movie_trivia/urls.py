from django.urls import path
from . import views

app_name = 'movie_trivia'

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.MovieList.as_view(), name='trivia'),
    path('questions/', views.QuestionsList.as_view(), name='questions'),
    path('movies/<str:topic>/q/', views.MovieQuestions.as_view(), name='movie-questions'),
    path('randomq/', views.RandomQuestion.as_view(), name='random-questions'),
    path('q/<int:pk>/<str:ans>', views.ValidateAnswers.as_view(), name='check-questions')
]

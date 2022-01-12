from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from .models import Movie, Questions
from .serializers import MovieSerializer, QuestionsSerializer, RandomQuestionSerializer
from rest_framework.response import Response

# Home page
def home(request):
    return HttpResponse('<h3>Movie API Endpoints Tests.</h3> <p>Go to /docs/ to see all the available methods.</p>')

# Create your views here.
class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class QuestionsList(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


# query a question for a specific movie - (problematic rn)
class MovieQuestions(APIView):
    def get(self, request, format=None, **kwargs):
        movie = Questions.objects.filter(movie__name=kwargs['topic']).order_by('?')[:1]
        serializer = QuestionsSerializer(movie, many=True)
        return Response(serializer.data)


# random question
class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.all().order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


# check whether the answers are correct
class ValidateAnswers(APIView):
    def get(self, request, format=None, **kwargs):
        correct_ans_obj = Questions.objects.filter(pk=kwargs['pk'])[0]
        correct_ans = correct_ans_obj.answer.lower()
        player_ans = kwargs['ans'].lower()
        serializer = {}
        serializer['Question'] = correct_ans_obj.title
        serializer['Answer'] = correct_ans
        if correct_ans == player_ans:
            serializer['Your answer is'] = True
            return Response(serializer)
        serializer['Your answer is'] = False
        return Response(serializer)




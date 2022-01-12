from rest_framework import serializers
from .models import Movie, Questions


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["name"]


class QuestionsSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Questions
        fields = ["movie", "title"]


class RandomQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ["pk", "movie", "title"]


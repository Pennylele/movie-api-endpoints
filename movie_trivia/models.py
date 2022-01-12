from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Questions(models.Model):

    class Meta:
        verbose_name = "Question" # setting up the admin UI display
        verbose_name_plural = "Questions"
        ordering = ['id']

    title = models.CharField(max_length=500, default="New Trivia", verbose_name="Trivia Question")
    movie = models.ForeignKey(Movie, default=1, on_delete=models.DO_NOTHING)
    answer = models.CharField(max_length=255, default="None")

    def __str__(self):
        return self.title
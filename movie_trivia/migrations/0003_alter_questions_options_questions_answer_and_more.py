# Generated by Django 4.0.1 on 2022-01-09 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_trivia', '0002_movie_questions_delete_movietrivia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ['id'], 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='questions',
            name='answer',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='questions',
            name='title',
            field=models.CharField(default='New Trivia', max_length=500, verbose_name='Trivia Question'),
        ),
    ]

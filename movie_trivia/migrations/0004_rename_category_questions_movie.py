# Generated by Django 4.0.1 on 2022-01-10 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_trivia', '0003_alter_questions_options_questions_answer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='category',
            new_name='movie',
        ),
    ]
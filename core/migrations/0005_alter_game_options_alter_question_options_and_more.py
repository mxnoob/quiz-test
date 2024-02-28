# Generated by Django 4.2.10 on 2024-02-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_game_questions_alter_question_answers"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="game",
            options={},
        ),
        migrations.AlterModelOptions(
            name="question",
            options={},
        ),
        migrations.AlterField(
            model_name="game",
            name="questions",
            field=models.ManyToManyField(to="core.question"),
        ),
        migrations.AlterField(
            model_name="question",
            name="answers",
            field=models.ManyToManyField(to="core.answer"),
        ),
    ]

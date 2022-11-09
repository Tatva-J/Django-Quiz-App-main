# Generated by Django 4.1.3 on 2022-11-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hint", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=250)),
                ("answer", models.CharField(max_length=100)),
                ("level", models.CharField(max_length=10)),
                ("points", models.IntegerField(default=3)),
                ("option_one", models.CharField(max_length=100)),
                ("option_two", models.CharField(max_length=100)),
                ("option_three", models.CharField(max_length=100)),
                ("option_four", models.CharField(max_length=100)),
                ("option_five", models.CharField(max_length=100)),
                ("hint_one", models.CharField(max_length=200)),
                ("hint_two", models.CharField(max_length=200)),
            ],
        ),
    ]

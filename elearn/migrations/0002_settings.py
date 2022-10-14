# Generated by Django 4.1 on 2022-10-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elearn", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_batches_boolean", models.BooleanField()),
                ("number_of_books_boolean", models.BooleanField()),
                ("number_of_teachers_boolean", models.BooleanField()),
            ],
        ),
    ]
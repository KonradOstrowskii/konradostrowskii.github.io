# Generated by Django 4.1.7 on 2023-03-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resume",
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
                ("name", models.CharField(max_length=100)),
                ("photo", models.ImageField(upload_to="photos")),
                ("education", models.TextField()),
                ("experience", models.TextField()),
                ("skills", models.TextField()),
            ],
        ),
    ]
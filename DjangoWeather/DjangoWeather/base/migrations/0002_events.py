# Generated by Django 5.0.4 on 2024-04-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("nom", models.CharField(max_length=100)),
                ("multiplicateur", models.FloatField()),
                ("lancers", models.IntegerField()),
                ("probabilite", models.FloatField()),
            ],
        ),
    ]

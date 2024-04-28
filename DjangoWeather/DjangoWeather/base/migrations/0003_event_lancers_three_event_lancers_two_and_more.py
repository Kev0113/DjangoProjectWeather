# Generated by Django 5.0.4 on 2024-04-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_events"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="lancers_three",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="event",
            name="lancers_two",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="event",
            name="multiplicateur_three",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="event",
            name="multiplicateur_two",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="event",
            name="lancers",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="event",
            name="multiplicateur",
            field=models.FloatField(default=0),
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-09 08:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_movie_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 9, 8, 13, 3, 68677, tzinfo=utc)),
        ),
    ]

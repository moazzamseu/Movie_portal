# Generated by Django 3.0.7 on 2020-06-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-13 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_cast'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('WL', 'WATCH LINK'), ('DL', 'DOWNLOAD LINK')], max_length=2)),
                ('links', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='movie.Movie')),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-14 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20200613_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=10),
        ),
    ]

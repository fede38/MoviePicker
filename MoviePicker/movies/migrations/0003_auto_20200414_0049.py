# Generated by Django 3.0.5 on 2020-04-14 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200412_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_rating',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
        ),
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='rotten_rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='movie',
            name='watched',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='year_of_release',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
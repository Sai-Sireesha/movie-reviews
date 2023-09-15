# Generated by Django 4.0 on 2023-09-12 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='crew',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='reviews',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='storyline',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='movie',
            name='teaser',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='user_rating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

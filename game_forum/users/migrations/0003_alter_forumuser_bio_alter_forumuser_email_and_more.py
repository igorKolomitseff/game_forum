# Generated by Django 5.0.6 on 2024-06-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_forumuser_bio_alter_forumuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumuser',
            name='bio',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='favorite_games',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Любимые игры'),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='favorite_genres',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Любимые жанры'),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='location',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Местоположение'),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='nickname',
            field=models.CharField(max_length=150, unique=True, verbose_name='Никнейм'),
        ),
    ]

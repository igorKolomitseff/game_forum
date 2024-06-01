# Generated by Django 5.0.6 on 2024-06-01 12:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор темы'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum', verbose_name='Форум'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]

from django.contrib.auth.models import AbstractUser
from django.db import models


class ForumUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта'
    )
    nickname = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Никнейм'
    )
    bio = models.TextField(
        blank=True,
        default='',
        verbose_name='Описание'
    )
    favorite_genres = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name='Любимые жанры'
    )
    favorite_games = models.CharField(
        max_length=255,
        blank=True,
        default='',
        verbose_name='Любимые игры'
    )
    location = models.CharField(
        max_length=150,
        blank=True,
        default='',
        verbose_name='Местоположение'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'nickname')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('nickname',)

    def __str__(self):
        return self.nickname

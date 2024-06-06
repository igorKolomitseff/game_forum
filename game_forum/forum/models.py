from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from slugify import slugify


TEXT_LENGTH = 50


def get_slug(instance):
    return slugify(instance.title)


class TimeModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    updated_at = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        verbose_name='Обновлено'
    )

    class Meta:
        abstract = True


class TitleSlugModel(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    slug = AutoSlugField(
        populate_from=get_slug,
        unique=True,
        always_update=True
    )

    class Meta:
        abstract = True


class Category(TitleSlugModel):
    description = models.TextField(
        blank=True,
        default='',
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

    def __str__(self):
        return (
            f'{self.title[:TEXT_LENGTH]}. '
            f'{self.description[:TEXT_LENGTH]}.'
        )


class Forum(TitleSlugModel):
    description = models.TextField(
        blank=True,
        default='',
        verbose_name='Описание'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'форум'
        verbose_name_plural = 'Форумы'
        default_related_name = 'forums'
        ordering = ('title',)

    def __str__(self):
        return (
            f'{self.title[:TEXT_LENGTH]}. '
            f'{self.description[:TEXT_LENGTH]}. | '
            f'В категории {self.category}'
        )


class Topic(TimeModel, TitleSlugModel):
    forum = models.ForeignKey(
        Forum,
        on_delete=models.CASCADE,
        verbose_name='Форум'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор темы'
    )

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'Темы'
        ordering = ('-created_at',)
        default_related_name = 'topics'

    def __str__(self):
        return (
            f'{self.title[:TEXT_LENGTH]}. | '
            f'Тема от {self.author} | '
            f'{self.created_at.strftime("%Y-%m-%d %H:%M")} | '
            f'в форуме {self.forum}'
        )


class Post(TimeModel):
    text = models.TextField()
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор публикации'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('created_at',)
        default_related_name = 'posts'

    def __str__(self):
        return (
            f'{self.text[:TEXT_LENGTH]}. | '
            f'Публикация от {self.author.nickname} | '
            f'{self.created_at.strftime("%Y-%m-%d %H:%M")}'
        )

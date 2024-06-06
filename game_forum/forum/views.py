from django.shortcuts import get_object_or_404, render

from .models import Category, Forum, Post, Topic


def index(request):
    return render(request, 'forum/index.html', {
        'categories': Category.objects.prefetch_related('forums'),
    })


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'forum/category_detail.html', {
        'category': category,
        'forums_list': category.forums.all(),
    })


def forum_detail(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    return render(request, 'forum/forum_detail.html', {
        'forum': forum,
        'topics_list': forum.topics.all(),
    })


def topic_detail(request, topic_slug):
    topic = get_object_or_404(
        Topic.objects.select_related('author'),
        slug=topic_slug
    )
    return render(request, 'forum/topic_detail.html', {
        'topic': topic,
        'posts_list': topic.posts.select_related('author'),
    })

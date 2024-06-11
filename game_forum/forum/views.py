from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm, TopicForm
from .models import Category, Forum, Post, Topic


def index(request):
    return render(request, 'forum/index.html', {
        'categories': Category.objects.prefetch_related('forums'),
    })


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'forum/category_detail.html', {
        'category': category,
        'forums': category.forums.all(),
    })


def forum_detail(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    return render(request, 'forum/forum_detail.html', {
        'forum': forum,
        'topics': forum.topics.all(),
    })


def topic_detail(request, topic_slug, post_id=None):
    topic = get_object_or_404(
        Topic.objects.select_related('author'),
        slug=topic_slug
    )
    if post_id is not None:
        post_instance = get_object_or_404(Post, pk=post_id)
    else:
        post_instance = None
    if '/delete_post/' in request.path:
        form = PostForm(instance=post_instance)
        if request.method == 'POST':
            post_instance.delete()
            return redirect('forum:topic_detail', topic_slug=topic_slug)
    else:
        form = PostForm(request.POST or None, instance=post_instance)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.topic = topic
        form.save()
        return redirect('forum:topic_detail', topic_slug=topic_slug)
    return render(request, 'forum/topic_detail.html', {
        'topic': topic,
        'forum': topic.forum,
        'posts': topic.posts.select_related('author'),
        'form': form,
    })


def topic_create(request, forum_slug):
    forum = get_object_or_404(Forum, slug=forum_slug)
    topic_form = TopicForm(request.POST or None)
    post_form = PostForm(request.POST or None)
    if topic_form.is_valid() and post_form.is_valid():
        topic = topic_form.save(commit=False)
        topic.forum = forum
        topic.author = request.user
        topic_form.save()

        post = post_form.save(commit=False)
        post.author = request.user
        post.topic = topic
        post_form.save()
        return redirect('forum:topic_detail', topic_slug=topic.slug)
    return render(request, 'forum/topic_create.html', {
        'topic_form': topic_form,
        'post_form': post_form,
    })


def topic_edit(request, forum_slug, topic_slug):
    topic_instance = get_object_or_404(Topic, slug=topic_slug)
    topic_form = TopicForm(request.POST or None, instance=topic_instance)
    if topic_form.is_valid():
        topic_form.save()
        return redirect(
            'forum:topic_detail',
            topic_slug=topic_form.instance.slug
        )
    return render(request, 'forum/topic_create.html', {
        'topic_form': topic_form,
    })


def topic_delete(request, forum_slug, topic_slug):
    topic_instance = get_object_or_404(Topic, slug=topic_slug)
    topic_form = TopicForm(instance=topic_instance)
    if request.method == 'POST':
        topic_instance.delete()
        return redirect(
            'forum:forum_detail',
            forum_slug=forum_slug
        )
    return render(request, 'forum/topic_create.html', {
        'topic_form': topic_form,
    })

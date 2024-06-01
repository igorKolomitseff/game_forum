from django.shortcuts import render

from .models import Category, Forum, Post, Topic


def index(request):
    return render(request, 'forum/index.html', {
        'categories': Category.objects.prefetch_related('forums'),
    })

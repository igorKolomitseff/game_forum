from django.contrib import admin

from .models import Category, Forum, Post, Topic


admin.site.register(Category)
admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Topic)

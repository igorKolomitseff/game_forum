from django.urls import path

from .import views


app_name = 'forum'

urlpatterns = [
    path('',
         views.index,
         name='index'),
    path('categories/<slug:category_slug>/',
         views.category_detail,
         name='category_detail'),
    path('forums/<slug:forum_slug>/',
         views.forum_detail,
         name='forum_detail'),
    path(
        'topics/<slug:topic_slug>/',
        views.topic_detail,
        name='topic_detail'
    )
]

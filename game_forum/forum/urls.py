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
    path('forums/<slug:forum_slug>/create_topic/',
         views.topic_create,
         name='create_topic'),
    path('forums/<slug:forum_slug>/edit_topic/<slug:topic_slug>/',
         views.topic_edit,
         name='edit_topic'),
    path('forums/<slug:forum_slug>/delete_topic/<slug:topic_slug>/',
         views.topic_delete,
         name='delete_topic'),
    path('topics/<slug:topic_slug>/',
         views.topic_detail,
         name='topic_detail'),
    path('topics/<slug:topic_slug>/edit_post/<int:post_id>/',
         views.topic_detail,
         name='edit_post'),
    path('topics/<slug:topic_slug>/delete_post/<int:post_id>/',
         views.topic_detail,
         name='delete_post'),
]

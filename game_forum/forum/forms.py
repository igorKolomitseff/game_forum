from django.forms import ModelForm

from .models import Post, Topic


class TopicForm(ModelForm):

    class Meta:
        model = Topic
        fields = ('title',)


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('text',)

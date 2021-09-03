from django.contrib import admin
from .models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'desc', 'url_news', 'post_img', 'created_date']

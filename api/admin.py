from django.contrib import admin
from api.models import articles, movies
# Register your models here.


@admin.register(articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'comment', 'author', 'pushdate', 'article_coverimg')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author', 'comment')  # 搜索字段
    date_hierarchy = 'pushdate'  # 详细时间分层筛选　
    ordering = ('id', 'pushdate',)

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 30


@admin.register(movies)
class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'comment', 'author', 'pushdate', 'movie_coverimg', 'movie')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author', 'comment')  # 搜索字段
    date_hierarchy = 'pushdate'  # 详细时间分层筛选　
    ordering = ('id', 'pushdate',)

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 30

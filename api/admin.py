from django.contrib import admin
from api.models import articles, movies

# Register your models here.
admin.site.site_header = '新蝶资源管理系统'
admin.site.site_title = '新蝶|新媒体'

@admin.register(articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'comment', 'author', 'pushdate', 'article_coverimg')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author', 'comment')  # 搜索字段
    date_hierarchy = 'pushdate'  # 详细时间分层筛选　
    ordering = ('id', 'pushdate',)

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 30

    class Media:
        js = [
            '/static/tiny_mce/tiny_mce_src.js',
            '/static/tiny_mce/tiny_mce_config.js',
        ]

@admin.register(movies)
class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'comment', 'author', 'pushdate', 'movie_coverimg', 'movie')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author', 'comment')  # 搜索字段
    date_hierarchy = 'pushdate'  # 详细时间分层筛选　
    ordering = ('id', 'pushdate',)

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 30

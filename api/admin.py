from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.site_header = '新蝶资源管理系统'
admin.site.site_title = '新蝶|新媒体'

@admin.register(articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'title', 'comment', 'author', 'pushdate', 'article_coverimg', 'is_pub')
    list_display_links = ('article_id', 'title')
    search_fields = ('title', 'author', 'comment')  # 搜索字段
    date_hierarchy = 'pushdate'  # 详细时间分层筛选　
    ordering = ('article_id', 'pushdate',)

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 30

    class Media:
        js = [
            '/static/tiny_mce/tiny_mce_src.js',
            '/static/tiny_mce/tiny_mce_config.js',
        ]

@admin.register(movies)
class MovieeAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'title', 'comment', 'author', 'pushdate', 'movie_coverimg', 'movie', 'is_pub')
    list_display_links = ('movie_id', 'title')
    search_fields = ('title', 'author', 'comment')  # 搜索字段
    date_hierarchy = 'pushdate'  # 详细时间分层筛选　
    ordering = ('movie_id', 'pushdate',)

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 30


@admin.register(article_opt_log)
class aritcle_opt_logAdmin(admin.ModelAdmin):
    list_display = ('art_opt_id', 'opt_content')
    search_fields = ('art_opt_id', 'opt_content', 'user_id')
    ordering = ('art_opt_id', 'opt_time')

    list_per_page = 30



@admin.register(movie_opt_log)
class movie_opt_logAdmin(admin.ModelAdmin):
    list_display = ('mov_opt_id', 'opt_content')
    search_fields = ('mov_opt_id', 'opt_content', 'user_id')
    ordering = ('mov_opt_id', 'opt_time')

    list_per_page = 30


@admin.register(users)
class usersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_realname', 'user_reg_time', 'user_status')
    search_fields = ('user_id', 'user_name', 'user_realname')
    ordering = ('user_id', 'user_reg_time')

    list_per_page = 30
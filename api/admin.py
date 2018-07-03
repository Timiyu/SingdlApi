from django.contrib import admin
from api.models import articles, moves
# Register your models here.

@admin.register(articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'pushdate')

@admin.register(moves)
class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'pushdate')



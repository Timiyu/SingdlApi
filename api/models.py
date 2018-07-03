# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.

class articles(models.Model):
    author = models.CharField(max_length=20, verbose_name='文章作者')
    title = models.CharField(max_length=20, verbose_name='文章标题')
    article_coverimg = models.ImageField(upload_to='articleimage', max_length=100, null=True, verbose_name='文章封面图片地址')
    comment = models.CharField(max_length=200, verbose_name='摘要')
    content = models.TextField(default='', verbose_name='文章内容')
    pushdate = models.DateTimeField(auto_now=True, verbose_name='发布时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = "文章"


class movies(models.Model):
    author = models.CharField(max_length=20, verbose_name='视频作者')
    title = models.CharField(max_length=20, verbose_name='视频标题')
    movie_coverimg = models.ImageField(upload_to='movieimage', max_length=100, null=True, verbose_name='视频封面图片地址')
    comment = models.CharField(max_length=200, verbose_name='摘要')
    movie = models.FileField(upload_to='movie', null=True, verbose_name='视频地址')
    pushdate = models.DateTimeField(auto_now=True, verbose_name='发布时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = "视频"

# -*- coding:utf-8 -*-
from django.db import models
import django.utils.timezone as timezone
from tinymce.models import HTMLField


# Create your models here.

class articles(models.Model):
    article_id = models.BigAutoField(primary_key=True, verbose_name='文章编号')
    author = models.CharField(max_length=20, verbose_name='文章作者')
    title = models.CharField(max_length=20, verbose_name='文章标题')
    comment = models.CharField(max_length=200, verbose_name='摘要')
    content = HTMLField(max_length=20000, verbose_name='文章内容')
    article_coverimg = models.ImageField(upload_to='articleimage', max_length=100, null=True, verbose_name='文章封面图片地址')
    pushdate = models.DateTimeField(auto_now=True, verbose_name='发布时间')
    is_pub = models.BooleanField(choices=((False, '否'), (True, '是')), verbose_name='是否立即发布', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = "文章"


class article_opt_log(models.Model):
    art_opt_id = models.BigAutoField(primary_key=True, verbose_name='文章操作编号')
    article_id = models.ForeignKey('articles', null=True, verbose_name='文章编号', on_delete=False)
    user_id = models.ForeignKey('users', null=True, verbose_name='用户编号', on_delete=False)
    opt_content = models.CharField(null=True, max_length=400, verbose_name='操作内容')
    opt_type = models.IntegerField(choices=((1, '浏览'), (2, '关注')), null=True, verbose_name='操作类型')
    opt_time = models.DateTimeField(auto_now=True, null=True, verbose_name='操作时间')

    def __str__(self):
        return self.opt_content

    class Meta:
        verbose_name = '文章操作记录'
        verbose_name_plural = "文章操作记录"



class movies(models.Model):
    movie_id = models.BigAutoField(primary_key=True, verbose_name='视频编号')
    author = models.CharField(max_length=20, verbose_name='视频作者')
    title = models.CharField(max_length=20, verbose_name='视频标题')
    movie_coverimg = models.ImageField(upload_to='movieimage', max_length=100, null=True, verbose_name='视频封面图片地址')
    comment = models.CharField(max_length=200, verbose_name='摘要')
    movie = models.FileField(upload_to='movie', null=True, verbose_name='视频地址')
    pushdate = models.DateTimeField(auto_now=True, verbose_name='发布时间')
    is_pub = models.BooleanField(choices=((False, '否'), (True, '是')), verbose_name='是否立即发布', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = "视频"



class movie_opt_log(models.Model):
    mov_opt_id = models.BigAutoField(primary_key=True, verbose_name='视频操作编号')
    movie_id = models.ForeignKey('movies', null=True, verbose_name='视频编号', on_delete=False)
    user_id = models.ForeignKey('users', null=True, verbose_name='用户编号', on_delete=False)
    opt_content = models.CharField(null=True, max_length=400, verbose_name='操作内容')
    opt_type = models.IntegerField(choices=((1, '浏览'), (2, '关注')), null=True, verbose_name='操作类型')
    opt_time = models.DateTimeField(auto_now=True, null=True, verbose_name='操作时间')

    def __str__(self):
        return self.opt_content

    class Meta:
        verbose_name = '视频操作记录'
        verbose_name_plural = "视频操作记录"


class users(models.Model):
    user_id = models.BigAutoField(primary_key=True, verbose_name='用户编号')
    user_name = models.CharField(max_length=10, verbose_name='用户名')
    user_password = models.CharField(max_length=200, verbose_name='密码')
    user_realname = models.CharField(max_length=20, verbose_name='用户真实姓名')
    user_phone = models.CharField(max_length=11, verbose_name='用户手机号')
    user_qq = models.CharField(max_length=20, verbose_name='用户QQ号')
    user_status = models.IntegerField(choices=((0, '未登录'), (1, '已登录')), verbose_name='登录状态')
    user_reg_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'APP用户'
        verbose_name_plural = "APP用户"

class feedback(models.Model):
    feed_id = models.BigAutoField(primary_key=True, verbose_name='反馈编号')
    user_id = models.ForeignKey('users', null=True, on_delete=False, verbose_name='用户编号', default='匿名')
    feedback = models.CharField(max_length=400, verbose_name='反馈内容')
    feed_time = models.DateTimeField(default=timezone.now, verbose_name='反馈时间')

    def __str__(self):
        return self.feedback

    class Meta:
        verbose_name = '反馈'
        verbose_name_plural = "反馈"


# Generated by Django 2.0.6 on 2018-07-03 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180703_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='articlecoverimg',
            new_name='article_coverimg',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='moviecoverimg',
            new_name='movie_coverimg',
        ),
    ]

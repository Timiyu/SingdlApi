# Generated by Django 2.0.6 on 2018-07-03 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='articlecoverimgurl',
            new_name='articlecoverimg',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='moviecoverimgurl',
            new_name='moviecoverimg',
        ),
    ]

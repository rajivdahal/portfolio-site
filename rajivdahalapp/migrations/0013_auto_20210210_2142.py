# Generated by Django 3.1.1 on 2021-02-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rajivdahalapp', '0012_mainpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpost',
            name='content',
        ),
        migrations.RemoveField(
            model_name='mainpost',
            name='description',
        ),
        migrations.RemoveField(
            model_name='mainpost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='mainpost',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='mainpost',
            name='title',
        ),
        migrations.AddField(
            model_name='mainpost',
            name='main_content',
            field=models.CharField(default='', max_length=20000, verbose_name='insert main content to show on left side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='main_description',
            field=models.CharField(default='', max_length=2000, verbose_name='insert main description to show on left side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='main_image',
            field=models.ImageField(blank=True, default='yy.jpg', upload_to='postimage', verbose_name='insert main image to show on left side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='main_title',
            field=models.CharField(default='', max_length=200, verbose_name='insert main title to show on left side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='right_down_content',
            field=models.CharField(default='', max_length=20000, verbose_name='insert secondary2 content to show on right down side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='right_down_description',
            field=models.CharField(default='', max_length=2000, verbose_name='insert secondary2 description to show on right down side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='right_down_image',
            field=models.ImageField(blank=True, default='pp.jpg', upload_to='postimage', verbose_name='insert secondary2 image to show on right down side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='right_down_title',
            field=models.CharField(default='', max_length=200, verbose_name='insert secondary2 title to show on right down side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='right_up_content',
            field=models.CharField(default='', max_length=20000, verbose_name='insert secondary1 content to show on right up side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='right_up_description',
            field=models.CharField(default='', max_length=2000, verbose_name='insert secondary1 description to show on right up side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='right_up_image',
            field=models.ImageField(blank=True, default='jj.jpg', upload_to='postimage', verbose_name='insert secondary1 image to show on right up side'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='right_up_title',
            field=models.CharField(default='', max_length=200, verbose_name='insert secondary1 title to show on right up side'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-12-28 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rajivdahalapp', '0009_post_bannerimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='bannerimage',
        ),
    ]

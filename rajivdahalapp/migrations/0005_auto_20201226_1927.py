# Generated by Django 3.1.1 on 2020-12-26 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rajivdahalapp', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='tt.jpg', upload_to='postimage'),
        ),
    ]

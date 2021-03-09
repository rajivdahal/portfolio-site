# Generated by Django 3.1.1 on 2020-12-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rajivdahalapp', '0006_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=2000)),
                ('image', models.ImageField(blank=True, default='tt.jpg', upload_to='postimage')),
            ],
        ),
    ]
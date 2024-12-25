# Generated by Django 5.1.4 on 2024-12-13 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

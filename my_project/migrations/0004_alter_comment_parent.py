# Generated by Django 5.1.4 on 2024-12-12 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_project', '0003_article_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_project.comment'),
        ),
    ]
# Generated by Django 4.2 on 2024-05-09 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_rename_like_count_articlelike_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlelike',
            name='like',
        ),
    ]
# Generated by Django 4.2 on 2024-05-07 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like_count',
        ),
    ]

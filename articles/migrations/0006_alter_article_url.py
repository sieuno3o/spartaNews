# Generated by Django 4.2 on 2024-05-09 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_articlelike_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

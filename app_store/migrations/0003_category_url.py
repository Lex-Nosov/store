# Generated by Django 4.2 on 2023-12-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0002_category_name_category_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.SlugField(default=models.TextField(max_length=50), max_length=100),
        ),
    ]

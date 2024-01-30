# Generated by Django 4.2 on 2023-12-27 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0004_alter_review_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('first_title', models.TextField(blank=True, max_length=50)),
                ('first_description', models.TextField(blank=True, max_length=1000)),
                ('second_title', models.TextField(blank=True, max_length=50)),
                ('second_description', models.TextField(blank=True, max_length=1000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_store.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
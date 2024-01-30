# Generated by Django 4.2.5 on 2023-11-17 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, max_length=10)),
                ('discount', models.PositiveIntegerField()),
                ('description_for_cart', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='static/img/')),
                ('stock', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('archived', models.BooleanField(default=False)),
                ('category_field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='app_store.category')),
            ],
            options={
                'verbose_name': 'products',
                'verbose_name_plural': 'products',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('article', models.TextField(blank=True, max_length=100)),
                ('country_manufacture', models.TextField(blank=True, max_length=100)),
                ('product_life', models.TextField(blank=True, max_length=100)),
                ('warranty_period', models.TextField(blank=True, max_length=100)),
                ('operating_system', models.TextField(blank=True, max_length=100)),
                ('case_material', models.TextField(blank=True, max_length=100)),
                ('weight', models.TextField(blank=True, max_length=100)),
                ('dimensions', models.TextField(blank=True, max_length=100)),
                ('processor', models.TextField(blank=True, max_length=100)),
                ('number_processor_cores', models.TextField(blank=True, max_length=100)),
                ('ram', models.TextField(blank=True, max_length=100)),
                ('integrated', models.TextField(blank=True, max_length=100)),
                ('internal_memory', models.TextField(blank=True, max_length=100)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app_store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('first_title', models.TextField(blank=True, max_length=50)),
                ('first_description', models.TextField(blank=True, max_length=1000)),
                ('second_title', models.TextField(blank=True, max_length=50)),
                ('second_description', models.TextField(blank=True, max_length=1000)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app_store.product')),
            ],
        ),
    ]

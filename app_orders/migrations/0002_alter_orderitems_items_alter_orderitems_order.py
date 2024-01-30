# Generated by Django 4.2.5 on 2023-12-13 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0002_category_name_category_ru'),
        ('app_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_store.product'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_orders.order'),
        ),
    ]
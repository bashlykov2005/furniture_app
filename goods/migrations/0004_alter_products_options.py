# Generated by Django 5.0 on 2024-06-17 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_rename_prise_products_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]

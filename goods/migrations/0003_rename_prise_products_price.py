# Generated by Django 5.0 on 2024-06-10 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='prise',
            new_name='price',
        ),
    ]
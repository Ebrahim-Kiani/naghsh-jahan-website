# Generated by Django 4.2.5 on 2024-03-17 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_module', '0009_rename_url_title_productcategory_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productbrand',
            old_name='url_title',
            new_name='slug',
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-21 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0003_auto_20190721_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='adalis_active',
            new_name='adilas_active',
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0002_auto_20190514_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='adalis_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='adilas_import_timestamp',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]

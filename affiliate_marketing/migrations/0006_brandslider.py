# Generated by Django 2.2.5 on 2019-11-04 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_storage', '0011_auto_20190424_1453'),
        ('affiliate_marketing', '0005_auto_20191104_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('title', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('subtitle', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('button_text', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('button_href', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('priority', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='affiliate_marketing.Brand')),
                ('image', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_slider_image', to='cloud_storage.CloudFile')),
            ],
        ),
    ]
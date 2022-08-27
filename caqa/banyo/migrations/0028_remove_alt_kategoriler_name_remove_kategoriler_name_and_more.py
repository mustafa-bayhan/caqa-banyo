# Generated by Django 4.0.2 on 2022-08-26 22:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banyo', '0027_alt_kategoriler_alter_kategoriler_alt_kategoriler_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alt_kategoriler',
            name='name',
        ),
        migrations.RemoveField(
            model_name='kategoriler',
            name='name',
        ),
        migrations.RemoveField(
            model_name='montaj_tipi',
            name='name',
        ),
        migrations.RemoveField(
            model_name='renkler',
            name='color_image',
        ),
        migrations.RemoveField(
            model_name='renkler',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ürün',
            name='color',
        ),
        migrations.RemoveField(
            model_name='ürün',
            name='image',
        ),
        migrations.RemoveField(
            model_name='ürün',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ürün',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='ürün_model',
            name='category_size',
        ),
        migrations.RemoveField(
            model_name='ürün_model',
            name='name',
        ),
        migrations.AddField(
            model_name='alt_kategoriler',
            name='isim',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='kategoriler',
            name='isim',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='montaj_tipi',
            name='isim',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='renkler',
            name='renk_ismi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='renkler',
            name='renk_resmi',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='ürün',
            name='isim',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ürün',
            name='renk',
            field=models.ManyToManyField(default='', related_name='color', to='banyo.Renkler'),
        ),
        migrations.AddField(
            model_name='ürün',
            name='ürün_modelleri',
            field=models.ManyToManyField(default='', related_name='type', to='banyo.Ürün_model'),
        ),
        migrations.AddField(
            model_name='ürün',
            name='ürün_resmi',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='ürün_model',
            name='isim',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ürün_model',
            name='model_ölçüleri',
            field=models.ManyToManyField(default='', to='banyo.Ölçüler'),
        ),
        migrations.AlterField(
            model_name='ürün',
            name='özellikler',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]

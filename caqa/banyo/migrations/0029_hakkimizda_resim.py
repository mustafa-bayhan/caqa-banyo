# Generated by Django 4.0.2 on 2022-08-27 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banyo', '0028_remove_alt_kategoriler_name_remove_kategoriler_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hakkimizda',
            name='resim',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-08-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banyo', '0012_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='çoks_satan',
            field=models.CharField(choices=[('evet', 'evet'), ('hayir', 'hayir')], default='hayir', max_length=200, null=True),
        ),
    ]

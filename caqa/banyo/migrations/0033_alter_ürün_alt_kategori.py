# Generated by Django 4.0.2 on 2022-09-04 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banyo', '0032_giris_resimleri_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ürün',
            name='alt_kategori',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Alt_kategori', to='banyo.alt_kategoriler'),
        ),
    ]

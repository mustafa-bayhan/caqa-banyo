# Generated by Django 4.0.2 on 2022-08-26 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banyo', '0024_renkler_delete_color_alter_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesajlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musteri_ismi', models.CharField(max_length=100, null=True, verbose_name='Ad Soyad')),
                ('mesaj', models.TextField(max_length=500, null=True, verbose_name='Yorum')),
                ('mail', models.EmailField(max_length=100, null=True)),
                ('telefon', models.CharField(max_length=12, null=True, verbose_name='telefon')),
            ],
        ),
        migrations.CreateModel(
            name='Montaj_tipi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Referanslar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(null=True, upload_to='image/references')),
                ('proje_adi', models.CharField(max_length=200, null=True)),
                ('firma', models.CharField(max_length=200, null=True)),
                ('adres', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ürün',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('özellikler', models.CharField(max_length=500, null=True)),
                ('acilis_sekli', models.ImageField(null=True, upload_to='image/')),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('görüntüleme', models.IntegerField(default=0)),
                ('alt_kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Alt_kategori', to='banyo.alt_kategori')),
                ('color', models.ManyToManyField(default='', null=True, related_name='color', to='banyo.Renkler')),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='banyo.kategoriler')),
                ('montaj_sekli', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='montaj', to='banyo.montaj_tipi')),
                ('product_type', models.ManyToManyField(default='', null=True, related_name='type', to='banyo.Ürün_model')),
            ],
        ),
        migrations.DeleteModel(
            name='Mesaj',
        ),
        migrations.RemoveField(
            model_name='product',
            name='alt_kategori',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='kategori',
        ),
        migrations.RemoveField(
            model_name='product',
            name='montaj_sekli',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.DeleteModel(
            name='Referans',
        ),
        migrations.DeleteModel(
            name='Montaj',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

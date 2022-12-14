# Generated by Django 4.0.2 on 2022-08-26 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banyo', '0022_ürün_model_delete_product_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('alt_kategoriler', models.ManyToManyField(default='', null=True, related_name='alt_kategori', to='banyo.Alt_kategori')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='banyo.kategoriler'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

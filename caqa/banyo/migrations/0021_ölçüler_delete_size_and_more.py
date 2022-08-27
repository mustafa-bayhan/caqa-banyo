# Generated by Django 4.0.2 on 2022-08-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banyo', '0020_alter_color_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ölçüler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ölçü', models.CharField(max_length=200, null=True)),
                ('giriş', models.CharField(default='', max_length=200, null=True)),
                ('yükseklik', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.AlterField(
            model_name='product_model',
            name='category_size',
            field=models.ManyToManyField(default='', null=True, to='banyo.Ölçüler'),
        ),
    ]

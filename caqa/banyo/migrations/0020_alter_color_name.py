# Generated by Django 4.0.2 on 2022-08-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banyo', '0019_mesaj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes_shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='image',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='Картинка одежды'),
        ),
    ]

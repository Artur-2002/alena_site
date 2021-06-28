# Generated by Django 2.2.6 on 2020-08-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_hair_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hair_img',
            name='image',
            field=models.ImageField(upload_to='static/hair/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='makeup_img',
            name='image',
            field=models.ImageField(upload_to='static/makeup/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='wedding_img',
            name='image',
            field=models.ImageField(upload_to='static/wedding/', verbose_name='Фото'),
        ),
    ]

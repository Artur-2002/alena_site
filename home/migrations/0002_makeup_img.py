# Generated by Django 2.2.6 on 2020-08-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makeup_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='makeup/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото макияжа',
                'verbose_name_plural': 'Фотки макияжа',
            },
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canciones', '0003_cancion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='imagen',
            field=models.ImageField(upload_to='imagenes'),
        ),
    ]
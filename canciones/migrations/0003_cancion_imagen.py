# Generated by Django 4.2.6 on 2023-11-06 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canciones', '0002_cancion_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAGUARETE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(upload_to='imagenes/'),
        ),
    ]

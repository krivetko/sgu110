# Generated by Django 3.2.9 on 2022-03-15 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tileimage',
            name='image_img',
            field=models.ImageField(upload_to=''),
        ),
    ]

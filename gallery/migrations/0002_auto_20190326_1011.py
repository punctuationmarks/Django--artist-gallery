# Generated by Django 2.1.7 on 2019-03-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerypost',
            name='image',
            field=models.ImageField(upload_to='gallery_pics'),
        ),
        migrations.AlterField(
            model_name='gallerypost',
            name='price',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-22 11:13

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_rename_product_image_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(upload_to='update/', verbose_name='blog_Image'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-24 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_remove_product_product_tagline_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Vegitables & Fruits', 'Vegitablesfruits'), ('MeatsSeafood', 'Meatsseafood'), ('BreakfastDairy', 'Breakfastdairy'), ('FrozenFood', 'Frozenfood')], max_length=20),
        ),
    ]
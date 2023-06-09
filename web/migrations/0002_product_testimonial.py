# Generated by Django 4.2.1 on 2023-06-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('English', 'English'), ('Malayalam', 'Malayalam'), ('Arabic', 'Arabic')], max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('publisher', models.CharField(max_length=50)),
                ('pdf', models.FileField(upload_to='pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=30)),
                ('testimonial_tittle', models.CharField(max_length=60)),
                ('testimonial_sentence', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]

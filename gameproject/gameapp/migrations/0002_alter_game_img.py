# Generated by Django 4.0.5 on 2022-06-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='img',
            field=models.ImageField(upload_to='games'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-28 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='_cart_id',
            new_name='cart_id',
        ),
    ]

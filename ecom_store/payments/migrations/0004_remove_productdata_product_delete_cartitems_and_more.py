# Generated by Django 4.1.7 on 2023-03-10 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_products_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdata',
            name='product',
        ),
        migrations.DeleteModel(
            name='cartItems',
        ),
        migrations.DeleteModel(
            name='productData',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestBuySearch', '0009_alter_vendorproduct_big_display_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorproduct',
            name='big_display_image',
            field=models.ImageField(max_length=500, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='vendorproduct',
            name='small_display_image',
            field=models.ImageField(max_length=500, upload_to='images/'),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_shop_address_zip_alter_shop_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_images_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0006_wish_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='wishes'),
        ),
    ]
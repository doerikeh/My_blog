# Generated by Django 3.0.2 on 2020-03-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='image_category',
            field=models.ImageField(blank=True, upload_to='static_cdn/images/'),
        ),
    ]

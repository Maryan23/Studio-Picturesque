# Generated by Django 3.2.8 on 2021-11-29 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0007_pictures_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pictures',
            options={'ordering': ['-pub_date']},
        ),
    ]
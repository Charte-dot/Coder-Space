# Generated by Django 3.2 on 2022-11-24 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_comment_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

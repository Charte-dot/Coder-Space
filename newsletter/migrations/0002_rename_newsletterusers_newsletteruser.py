# Generated by Django 3.2 on 2022-12-05 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsletterUsers',
            new_name='NewsletterUser',
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-22 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='flas_name',
            new_name='last_name',
        ),
    ]

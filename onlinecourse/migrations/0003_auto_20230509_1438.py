# Generated by Django 3.1.3 on 2023-05-09 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230324_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='correct',
            new_name='is_correct',
        ),
    ]

# Generated by Django 2.2.6 on 2021-06-21 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210621_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='username',
        ),
    ]

# Generated by Django 2.2.6 on 2021-06-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210621_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='institution',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='skills',
            field=models.CharField(default='', max_length=20),
        ),
    ]
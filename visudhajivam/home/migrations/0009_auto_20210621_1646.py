# Generated by Django 2.2.6 on 2021-06-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=12),
        ),
    ]

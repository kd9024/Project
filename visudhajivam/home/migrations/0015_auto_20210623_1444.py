# Generated by Django 2.2.6 on 2021-06-23 09:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210623_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myinfo',
            name='user1',
        ),
        migrations.AddField(
            model_name='myinfo',
            name='DOB',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='address',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='city',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='contact',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='country',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='email',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='first_name',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='institution',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='last_name',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='qualification',
            field=models.CharField(default='', max_length=90),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='skills',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='state',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='users',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='myinfo',
            name='zipcode',
            field=models.CharField(default='', max_length=12),
        ),
    ]

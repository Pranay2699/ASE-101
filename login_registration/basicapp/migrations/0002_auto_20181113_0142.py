# Generated by Django 2.1.2 on 2018-11-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='gender',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

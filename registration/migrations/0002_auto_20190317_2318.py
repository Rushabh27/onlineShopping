# Generated by Django 2.1.7 on 2019-03-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='userid',
        ),
        migrations.AddField(
            model_name='userdata',
            name='username',
            field=models.CharField(default='guest', max_length=100),
        ),
    ]
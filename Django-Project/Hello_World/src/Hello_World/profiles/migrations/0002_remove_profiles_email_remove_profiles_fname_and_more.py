# Generated by Django 5.0.2 on 2024-02-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='username',
        ),
        migrations.AddField(
            model_name='profiles',
            name='First_Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profiles',
            name='Last_Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profiles',
            name='Email',
            field=models.EmailField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profiles',
            name='Username',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]

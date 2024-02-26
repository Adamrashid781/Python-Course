# Generated by Django 5.0.2 on 2024-02-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, default='First Name', max_length=50)),
                ('lname', models.CharField(blank=True, default='Last Name', max_length=50)),
                ('email', models.EmailField(blank=True, default='Email', max_length=50)),
                ('username', models.CharField(blank=True, default='Username', max_length=50)),
            ],
        ),
    ]
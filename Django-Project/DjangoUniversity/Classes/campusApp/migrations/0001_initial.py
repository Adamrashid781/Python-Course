# Generated by Django 5.0.2 on 2024-03-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_name', models.CharField(blank=True, default='', max_length=60)),
                ('state', models.CharField(blank=True, default='', max_length=60)),
                ('campus_id', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'University Campus',
            },
        ),
    ]

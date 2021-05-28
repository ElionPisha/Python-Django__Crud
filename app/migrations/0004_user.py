# Generated by Django 3.1.2 on 2020-10-07 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201006_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birthday', models.CharField(max_length=8)),
                ('mobile_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

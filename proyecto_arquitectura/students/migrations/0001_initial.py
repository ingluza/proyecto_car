# Generated by Django 4.2.2 on 2023-06-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('identification', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('last_name', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('cellphone', models.CharField(default=None, max_length=15)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=240)),
            ],
        ),
    ]

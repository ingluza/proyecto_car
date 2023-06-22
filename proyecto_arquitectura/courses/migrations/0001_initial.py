# Generated by Django 4.2.2 on 2023-06-20 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0004_alter_teacher_identification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('description', models.TextField(null=True)),
                ('rating', models.CharField(null=True)),
                ('teacher_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
        ),
    ]
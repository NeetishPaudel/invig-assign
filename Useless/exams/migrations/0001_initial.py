# Generated by Django 2.2.24 on 2021-08-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('level', models.CharField(max_length=15)),
                ('manpower', models.PositiveSmallIntegerField()),
            ],
        ),
    ]

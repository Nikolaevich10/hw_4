# Generated by Django 3.2.6 on 2021-08-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210828_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=120, verbose_name='way')),
                ('timestamp', models.DateTimeField(verbose_name='time')),
                ('method', models.CharField(max_length=120, verbose_name='method')),
            ],
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='ИМЯ')),
                ('last_name', models.CharField(max_length=30, verbose_name='ФАМИЛИЯ')),
                ('email', models.EmailField(max_length=254, verbose_name='ПОЧТА')),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=100),
        ),
    ]
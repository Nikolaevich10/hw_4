import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    first_name = models.CharField(verbose_name='ИМЯ', max_length=30)
    last_name = models.CharField(verbose_name='ФАМИЛИЯ', max_length=30)
    email = models.EmailField(verbose_name='ПОЧТА')

    def __str__(self):
        return self.first_name, self.last_name, self.email


class Log(models.Model):
    path = models.CharField(verbose_name='way', max_length=120)
    timestamp = models.DateTimeField(verbose_name='time')
    method = models.CharField(verbose_name='method', max_length=120)

    def __str__(self):
        return self.path

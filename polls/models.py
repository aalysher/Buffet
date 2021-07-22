from datetime import datetime

from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Номер телефона', max_length=255)
    pin = models.CharField('Пин-код', max_length=6)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Номер телефона', max_length=255)
    course_id = models.ForeignKey("Course", on_delete=models.DO_NOTHING)
    pin = models.CharField('Пин-код', max_length=6)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField("Название курса", max_length=255)
    mentor = models.CharField("Ментор", max_length=255, blank=True, null=True)
    assistant = models.CharField("Ассистент", max_length=255, blank=True, null=True)
    classroom = models.CharField("Аудитория", max_length=255, blank=True, null=True)
    start_date = models.DateTimeField("Дата начало курса", auto_now_add=True)
    end_date = models.DateTimeField("Дата окончания курса", default=datetime(2999, 12, 31))
    price = models.FloatField("Цена")
    time = models.CharField('Время', max_length=50, default="08:00")

    def __str__(self):
        return self.name


class Operation(models.Model):
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    total_sum = models.FloatField()
    debt_sum = models.FloatField()
    pin = models.ForeignKey('Pin', on_delete=models.CASCADE)
    status = models.IntegerField(choices=[
        (1, 'Оплачен'),
        (2, 'Не оплачен'),
        (3, 'Списан')
    ])

    def __str__(self):
        return str(self.pin)


class Pin(models.Model):
    pin = models.CharField(primary_key=True, max_length=6)
    debt = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pin)


class OperationDetail(models.Model):
    amount = models.CharField(max_length=255)
    buffet = models.ForeignKey('Buffet', on_delete=models.CASCADE)
    operations = models.ForeignKey(Operation, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.operations)


class Buffet(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    price = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

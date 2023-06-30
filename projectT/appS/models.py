from django.db import models
from django.core import validators
# Create your models here.

class User_req(models.Model):
    STS = (('viewed', 'Просмотренно'),
           ('inQueue', 'В очереди'),
           ('rejected', 'Отказанно'))

    status = models.CharField(max_length=13, choices=STS, default='inQueue', verbose_name='Статус заявки')
    fname = models.CharField(max_length=33, verbose_name='Фамилия', validators=[validators.MinLengthValidator(2, message='Минимум 2 символа')])
    sname = models.CharField(max_length=33, verbose_name='Имя', validators=[validators.MinLengthValidator(2, message='Минимум 2 символа')])
    umail = models.EmailField(verbose_name='Электронная почта', validators=[validators.EmailValidator(message='Введите действительный адрес')])

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'
        # ordering = ['-fname']


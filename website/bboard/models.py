from django.db import models
from django.core import validators
from datetime import datetime
class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

class Bb(models.Model):
    def id_and_timeleft(self):
        # return 'example'
        time1 = str(self.published.today())
        time2 = str(self.published)
        time2 = time2[0:len(time2)-6]

        timedelta = datetime.strptime(time1, "%Y-%m-%d %H:%M:%S.%f") - datetime.strptime(time2, "%Y-%m-%d %H:%M:%S.%f")
        hours = round(timedelta.total_seconds() // 3600)
        days_count = hours // 24
        days_count2 = days_count * 24
        hours_count = hours - days_count2

        text_h = 'часов назад'
        if hours_count == 1:
            text_h = 'час назад'
        elif hours_count in (2, 3, 4):
            text_h = 'часа назад'

        return f'(Nº{self.id}) {days_count} дн. {hours_count} {text_h}'
        # return f'{hours, hours_count, time2}'

    id_and_timeleft.short_description = 'Номер и прошедшее время '

    KINDS = (('b', "Куплю"),
             ('s', "Продам"),
             ('c', "Обменяю"))
    kind = models.CharField(max_length=1, choices=KINDS, default='s', verbose_name="Вид")
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name='Загаловок', validators=[validators.MinLengthValidator(8, message='Минимум 10 символов')])
    content = models.TextField(null=True, blank=True, verbose_name='Контент')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


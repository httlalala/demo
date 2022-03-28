from django.db import models


class Schedule(models.Model):
    WEEKDAY_CHOICES = (
        (1, '星期一'),
        (2, '星期二'),
        (3, '星期三'),
        (4, '星期四'),
        (5, '星期五'),
        (6, '星期六'),
        (7, '星期日'),
    )

    week = models.SmallIntegerField(null=False, verbose_name='周次')
    weekday = models.SmallIntegerField(choices=WEEKDAY_CHOICES, null=False, verbose_name='星期')
    order = models.SmallIntegerField(null=False, verbose_name='节次')
    # time = models.DateTimeField(null=True,verbose_name='时间')

    class Meta:
        db_table = 'exchangecourse_schedule'
        verbose_name = '课程时间表'
        verbose_name_plural = verbose_name
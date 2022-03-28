from django.db import models

# Create your models here.
class CourseTime(models.Model):
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

    class Meta:
        db_table = 'exchangecourse_course_time'
        verbose_name = '课程时间表'
        verbose_name_plural = verbose_name


class Course(models.Model):
    name = models.CharField(max_length=128,null=False,verbose_name='课程名')
    teacher_id = models.ForeignKey("users.User",db_column='teacher_id',null=False,on_delete=models.CASCADE,verbose_name='教师id')
    class_id = models.ForeignKey("classes.Class",db_column='class_id',null=False,on_delete=models.CASCADE,verbose_name='班级id')
    week = models.SmallIntegerField(null=False,verbose_name='周次')
    WEEKDAY_CHOICES = (
        (1,'星期一'),
        (2,'星期二'),
        (3,'星期三'),
        (4,'星期四'),
        (5,'星期五'),
        (6,'星期六'),
        (7,'星期日'),
    )
    weekday = models.SmallIntegerField(choices=WEEKDAY_CHOICES,null=False,verbose_name='星期')
    order = models.SmallIntegerField(null=False,verbose_name='节次')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除标记')

    # schedule_id = models.ForeignKey('schedule.Schedule',null=True,db_column='schedule_id',on_delete=models.CASCADE,verbose_name='课程时间id')

    start_time = models.DateTimeField(auto_now_add=True,null=False, verbose_name='上课时间')
    end_time = models.DateTimeField(auto_now_add=True,null = False, verbose_name = '下课时间')

    class Meta:
        db_table = 'exchangecourse_course'
        verbose_name = '课程表'
        verbose_name_plural = verbose_name


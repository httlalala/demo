from django.db import models

# Create your models here.
class Class(models.Model):
    school_id = models.ForeignKey('schools.School', on_delete=models.CASCADE,db_column='school_id',verbose_name='学校id')
    GRADE_CHOICES = (
        (1, '一年级'),
        (2, '二年级'),
        (3, '三年级'),
        (4, '四年级'),
        (5, '五年级'),
        (6, '六年级'),
    )
    grade = models.SmallIntegerField(choices=GRADE_CHOICES,verbose_name='年级')
    class_number = models.SmallIntegerField(verbose_name='班号')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除标记')


    class Meta:
        db_table = 'exchangecourse_class'
        verbose_name = '班级表'
        verbose_name_plural = verbose_name
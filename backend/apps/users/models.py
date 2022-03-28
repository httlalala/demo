from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    # 删除不需要的字段
    first_name = None
    last_name = None
    email = None
    is_staff = None
    is_active = None
    date_joined =None
    # 我们需要的字段
    work_id = models.CharField(max_length=25,unique=True,null=True,verbose_name='工号')
    icon = models.ImageField(upload_to='users',null=True,verbose_name='头像')
    phone = models.CharField(max_length=11,null=False,verbose_name='电话')
    email = models.CharField(max_length=256,null=True,verbose_name='邮箱')
    GRADE_CHOICES = (
        (0,'普通用户'),
        (1,'一年级管理员'),
        (2,'二年级管理员'),
        (3,'三年级管理员'),
        (4,'四年级管理员'),
        (5,'五年级管理员'),
        (6,'六年级管理员'),
    )
    is_grade = models.SmallIntegerField(choices=GRADE_CHOICES,default=0,null=False,verbose_name='年级管理员')
    SUPER_CHOICES = (
        (0,'否'),
        (1,'是'),
    )
    is_super = models.SmallIntegerField(choices=GRADE_CHOICES,default=0,null=False,verbose_name='总管理员')
    is_active = models.BooleanField(default=True,verbose_name='有效用户')  #默认
    wechat = models.CharField(max_length=128,null=True,verbose_name='微信号')
    school_id = models.ForeignKey('schools.School',on_delete=models.CASCADE,db_column='school_id',verbose_name='学校id')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除标记')


    class Meta:
        db_table = 'exchangecourse_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        unique_together = (
            ('username', 'school_id'),
        )



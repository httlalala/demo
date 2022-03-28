from django.db import models

# Create your models here.
class SMSCode(models.Model):
    phone = models.CharField(max_length=11,null=False,unique=True,verbose_name='手机号')
    code = models.CharField(max_length=20,null=False,verbose_name='验证码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'exchangecourse_smscode'
        verbose_name = '短信验证码表'
        verbose_name_plural = verbose_name
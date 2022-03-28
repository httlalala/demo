from django.db import models

# Create your models here.

class Application(models.Model):
    applicant_course_id = models.ForeignKey('courses.Course',null=False,on_delete=models.CASCADE,related_name='applicant_course_id', db_column='applicant_course_id',verbose_name='申请课程id')
    reason = models.CharField(max_length=256,null=False,verbose_name='申请理由')
    APPLY_TYPE_CHOICES = (
        (0, '调课'),
        (1, '代课'),
    )
    type = models.SmallIntegerField(choices=APPLY_TYPE_CHOICES,null=False,default=0,verbose_name='申请类型')
    create_time = models.DateTimeField(auto_now_add=True,null=False, verbose_name='申请时间')
    target_course_id = models.ForeignKey('courses.Course', null=True,on_delete=models.CASCADE,related_name='target_course_id',db_column='target_course_id',verbose_name='目标课程id')
    handler_id = models.ForeignKey('users.User', null=True,on_delete=models.CASCADE,db_column='handler_id',verbose_name='处理人id')
    handle_time = models.DateTimeField(null=True,verbose_name='处理时间')
    fail_time = models.DateTimeField(null=False,verbose_name='到期时间')
    CONFIRM_CHOICES = (
        (0,'未确认'),
        (1,'确认且同意'),
        (2,'确认且拒绝'),
    )
    applicant_confirm = models.SmallIntegerField(choices=CONFIRM_CHOICES,null=False,default=0,verbose_name='申请方是否确认')
    solver_confirm = models.SmallIntegerField(choices=CONFIRM_CHOICES,null=False,default=0,verbose_name='目标方是否确认')
    overdue = models.BooleanField(null=False,default=False,verbose_name='是否过期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除标记')

    cancel_reason = models.CharField(max_length=256,null=True,verbose_name='拒绝原因')

    class Meta:
        db_table = 'exchangecourse_application'
        verbose_name = '申请表'
        verbose_name_plural = verbose_name

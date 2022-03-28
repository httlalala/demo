from django.db import models

# Create your models here.
class School(models.Model):
    province = models.CharField(max_length=128,verbose_name='省')
    city = models.CharField(max_length=128,verbose_name='市')
    region = models.CharField(max_length=128,verbose_name='区')
    address = models.CharField(max_length=256,verbose_name='详细地址')
    name = models.CharField(max_length=128,verbose_name='学校名')
    # week_diff_first = models.SmallIntegerField(default=0,null=True,verbose_name='上学期自然周差')
    # week_diff_second = models.SmallIntegerField(default=0,null=True,verbose_name='下学期自然周差')

    week_num = models.SmallIntegerField(default=20,null=False,verbose_name='本学期总周数')
    first_week_date = models.DateTimeField(null=True,verbose_name='第一周日期')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除标记')


    class Meta:
        db_table = 'exchangecourse_school'
        verbose_name = '学校表'
        verbose_name_plural = verbose_name
# import datetime
# School.objects.create(province="江苏省",city="无锡市",region="滨湖区",address="蠡湖大道1号",name="蒋王小学",week_num=20,first_week_date=datetime.datetime.now())
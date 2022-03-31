from django.db import models

# Create your models here.
class UploadRecord(models.Model):
    path = models.CharField(max_length=256,null=False,verbose_name='上传路径')
    uploader_id = models.ForeignKey('users.User',null=False,on_delete=models.CASCADE,verbose_name='上传者id',db_column='uploader_id')
    start_time = models.DateTimeField(null=False,verbose_name='启用日期')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除标记')

    class Meta:
        db_table = 'exchangecourse_upload_record'
        verbose_name = '上传记录表'
        verbose_name_plural = verbose_name

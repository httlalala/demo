

def task_test():
    with open('test.txt','a+') as f:
        f.write('*')


def task_update_overdue():
    import datetime
    from utils.timediff import utf2local
    import sys
    import os
    import django
    # 这两行很重要，用来寻找项目根目录，os.path.dirname要写多少个根据要运行的python文件到根目录的层数决定
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(BASE_DIR)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excourse_v1.settings')
    django.setup()
    from applications.models import Application
    applications = Application.objects.filter(overdue=0,type=0)
    for application in applications:
        # todo 判断是否过期: 当前日期 >= 申请课程的上课日期
        if datetime.datetime.now().date() >= utf2local(application.fail_time).date():
            application.overdue = 1
            application.save()

#
# def control_add():
#     import os
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     cron = CronTab(user='root')
#     job = cron.new(command='python %s'%os.path.join(BASE_DIR,'utils/crontab.py'), comment='id')
#     job.minute.every(1)
#     cron.write()
#
# def control_delete():
#     import os
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     del_cron = CronTab(user='root')
#     iter = del_cron.find_comment('id')
#     for job in iter:
#         del_cron.remove(job)
#     del_cron.write()
#
# def control_edit():
#     cron = CronTab(user='root')
#     iter_job = cron.find_comment('id')
#     for job in iter_job:
#         job.set_command("python bakcup.py --port=3306")
#     cron.write()
#
# def control_run():
#     cron = CronTab(user='root')
#     iter_job = cron.find_comment('data_list')
#     for job in iter_job:
#         out = job.run()
#
# if __name__ == '__main__':
#     task_test()
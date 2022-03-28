'''根据数据库course表生成本地文件'''
import datetime
import logging
from io import BytesIO
import pandas as pd
from django.http import HttpResponse

from applications.models import Application
from courses.models import Course
import os


def saveFile(week_start, week_end, path, is_application=False):
    try:
        if is_application:
            file_name = os.path.join(path, 'course_application_%s_%s.xls' % (str(week_start), str(week_end)))
            if os.path.exists(file_name):
                return file_name
            writer = pd.ExcelWriter(file_name)
            courses = Course.objects.filter(week__gte=week_start, week__lte=week_end).order_by('week', 'weekday',
                                                                                               'class_id__grade',
                                                                                               'class_id__class_number',
                                                                                               'order')
            data = courses.values('week', 'weekday', 'class_id__grade', 'class_id__class_number', 'order', 'name',
                                  'teacher_id__username')  # 这里可以格式化当前表和关联表的数据
            df = pd.DataFrame(data)
            df.rename(columns={'week': '周',
                               'weekday': '预约时间',
                               'class_id__grade': '年级',
                               'class_id__class_number': '班级',
                               'order': '节次',
                               'name': '课程',
                               'teacher_id__username': '授课教师',
                               },
                      inplace=True)  # 重定义列名 可修改任意列名
            df.to_excel(writer, index=False, sheet_name='course')
            data = Application.objects.all().values('applicant_course_id__teacher_id__username',
                                                    'applicant_course_id__class_id__grade',
                                                    'applicant_course_id__class_id__class_number',
                                                    'applicant_course_id__week',
                                                    'applicant_course_id__order',
                                                    'target_course_id__teacher_id__username',
                                                    'target_course_id__class_id__grade',
                                                    'target_course_id__class_id__class_number',
                                                    'target_course_id__week',
                                                    'target_course_id__order',
                                                    'type',
                                                    'solver_confirm',
                                                    'create_time',
                                                    'handle_time')
            df = pd.DataFrame(data)
            df.rename(columns={
                'applicant_course_id__teacher_id__username': '申请人',
                'applicant_course_id__class_id__grade': '申请年级',
                'applicant_course_id__class_id__class_number': '申请班级',
                'applicant_course_id__week': '申请周次',
                'applicant_course_id__order': '申请节次',
                'target_course_id__teacher_id__username': '目标人',
                'target_course_id__class_id__grade': '目标年级',
                'target_course_id__class_id__class_number': '目标班级',
                'target_course_id__week': '目标周次',
                'target_course_id__order': '目标节次',
                'type': '申请类型',
                'solver_confirm': '状态',
                'create_time': '申请时间',
                'handle_time': '处理时间'}, inplace=True)
            df.to_excel(writer, index=False, sheet_name='application')
            writer.save()
            writer.close()
            return file_name
        else:
            file_name = os.path.join(path, 'course_%s_%s.xls' % (str(week_start), str(week_end)))
            if os.path.exists(file_name):
                return file_name
            writer = pd.ExcelWriter(file_name)
            courses = Course.objects.filter(week__gte=week_start, week__lte=week_end).order_by('week', 'weekday',
                                                                                               'class_id__grade',
                                                                                               'class_id__class_number',
                                                                                               'order')
            data = courses.values('week', 'weekday', 'class_id__grade', 'class_id__class_number', 'order', 'name',
                                  'teacher_id__username')  # 这里可以格式化当前表和关联表的数据
            df = pd.DataFrame(data)
            df.rename(columns={'week': '周',
                               'weekday': '预约时间',
                               'class_id__grade': '年级',
                               'class_id__class_number': '班级',
                               'order': '节次',
                               'name': '课程',
                               'teacher_id__username': '授课教师',
                               },
                      inplace=True)  # 重定义列名 可修改任意列名
            df.to_excel(writer, index=False, sheet_name='course')
            writer.save()
            writer.close()
            return file_name
    except Exception as e:
        logging.info(e)
        return None
    # outfile = BytesIO()
    # courses = Course.objects.filter(week__gte=week_start, week__lte=week_end).order_by('week', 'weekday',
    #                                                                                    'class_id__grade',
    #                                                                                    'class_id__class_number',
    #                                                                                    'order')
    # data = courses.values('week', 'weekday', 'class_id__grade', 'class_id__class_number', 'order', 'name',
    #                       'teacher_id__username')  # 这里可以格式化当前表和关联表的数据
    # df = pd.DataFrame(data)
    # response = HttpResponse(content_type='application/vnd.ms-excel')
    # execl_name = 'courses_%s_%s.' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
    # df.rename(columns={'description': '描述', 'wanttime': '预约时间', 'overdue_time': '过期时间'}, inplace=True)  # 重定义列名 可修改任意列名
    # df.to_excel(outfile, index=False)
    # response.write(outfile.getvalue())


import time as TIME
import datetime
from django.db import transaction

from users.models import User
from classes.models import Class
from schools.models import School
from courses.models import Course
from utils.timediff import utc2local

'''

'''


def test():
    mapdict = {
        '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9
    }
    filename='course.xls'
    week_start = 1
    school = School.objects.get(id=1)
    school_id = 1
    week_num = school.week_num
    first_week_date = school.first_week_date

    import xlrd
    from tqdm import tqdm

    order_indexes = [4, 5, 7, 9, 10, 11]
    weekday_indexes = [3, 4, 5, 6, 7]

    book = xlrd.open_workbook(filename)

    class_list = book.sheet_names()
    for class_name in tqdm(class_list):
        print(class_name)
        sheet = book.sheet_by_name(class_name)
        # todo 拿到 学校
        try:
            school = School.objects.get(id=school_id)
        except School.DoesNotExist:
            return 0
        # todo 拿到 年级 和 班号
        grade = mapdict.get(class_name[0], None)
        class_number = int(class_name[1])
        # todo 如果班级不存在  那么新建班级
        try:
            class_obj = Class.objects.get(school_id=school, grade=grade, class_number=class_number)
        except Class.DoesNotExist:
            class_obj = Class.objects.create(school_id=school, grade=grade, class_number=class_number)

        try:
            with transaction.atomic():
                for j in range(len(weekday_indexes)):
                    for i in range(len(order_indexes)):
                        # todo 拿到这节课的  教师名字  课程名  星期 节次
                        course = sheet.cell_value(order_indexes[i], weekday_indexes[j])
                        if course.strip() != '':
                            weekday = j + 1
                            order = i + 1
                            course_name, teacher_name = course.split('\n')[0], course.split('\n')[1]
                            teacher_name = teacher_name.replace('(', '')
                            teacher_name = teacher_name.replace(')', '')
                            # todo 如果教师不存在  那么新建教师
                            try:
                                teacher_obj = User.objects.get(school_id=school, username=teacher_name)
                            except User.DoesNotExist:
                                teacher_obj = User.objects.create(phone='111111%s' % str(TIME.time())[-5:],
                                                                  school_id=school, username=teacher_name)
                                teacher_obj.set_password("123")
                                teacher_obj.save()
                            # todo 新建课程
                            for week in range(week_start, week_num + 1):
                                # try:
                                #     schedule = Schedule.objects.get(week=week, weekday=weekday, order=order)
                                # except Schedule.DoesNotExist:
                                #
                                #     schedule = Schedule.objects.create(week=week, weekday=weekday, order=order)

                                time_str = sheet.cell_value(order_indexes[i], 2).split('--')
                                time_list = []  # 上课时间，下课时间
                                for time in time_str:
                                    time=time.replace(" ","")
                                    time=time.replace("：", ":")
                                    time2datetime = datetime.datetime.strptime(time, '%H:%M')  # 文字转datetime
                                    # datetime 转 timedelta
                                    timediff = datetime.timedelta(weeks=week - 1, days=weekday - 1,
                                                                  hours=time2datetime.hour,
                                                                  minutes=time2datetime.minute)
                                    # 实际时间=第一周时间+timedelta
                                    time_list.append(utc2local(first_week_date + timediff))

                                try:
                                    course = Course.objects.get(teacher_id=teacher_obj,week=week, weekday=weekday, order=order)
                                    course.name = course_name
                                    course.teacher_id = teacher_obj
                                    course.class_id = class_obj
                                    course.start_time = time_list[0]
                                    course.end_time = time_list[1]
                                    course.save()
                                except Course.DoesNotExist:
                                    Course.objects.create(name=course_name, teacher_id=teacher_obj, class_id=class_obj,
                                                          week=week, weekday=weekday, order=order,
                                                          start_time=time_list[0], end_time=time_list[1])

        except Exception as e:
            raise e
            return 0

    return 1


def generateData(school_id, filename, week_start):
    mapdict = {
        '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9
    }




    import xlrd
    from tqdm import tqdm

    order_indexes = [4, 5, 7, 9, 10, 11]
    weekday_indexes = [3, 4, 5, 6, 7]

    book = xlrd.open_workbook(filename)

    class_list = book.sheet_names()
    for class_name in tqdm(class_list):
        sheet = book.sheet_by_name(class_name)
        # todo 拿到 学校id
        try:
            school = School.objects.get(id=school_id)
            week_num = school.week_num
            first_week_date = school.first_week_date
        except School.DoesNotExist:
            return 0
        # todo 拿到 年级 和 班号
        grade = mapdict.get(class_name[0], None)
        class_number = int(class_name[1])
        # todo 如果班级不存在  那么新建班级
        try:
            class_obj = Class.objects.get(school_id=school, grade=grade, class_number=class_number)
        except Class.DoesNotExist:
            class_obj = Class.objects.create(school_id=school, grade=grade, class_number=class_number)
        try:
            with transaction.atomic():
                for j in range(len(weekday_indexes)):
                    for i in range(len(order_indexes)):
                        # todo 拿到这节课的  教师名字  课程名  星期 节次
                        course = sheet.cell_value(order_indexes[i], weekday_indexes[j])
                        if course.strip() != '':
                            weekday = j + 1
                            order = i + 1
                            course_name, teacher_name = course.split('\n')[0], course.split('\n')[1]
                            teacher_name = teacher_name.replace('(', '')
                            teacher_name = teacher_name.replace(')', '')
                            # todo 如果教师不存在  那么新建教师
                            try:
                                teacher_obj = User.objects.get(school_id=school, username=teacher_name)
                            except User.DoesNotExist:
                                teacher_obj = User.objects.create(phone='111111%s' % str(TIME.time())[-5:],
                                                                  school_id=school, username=teacher_name)
                                teacher_obj.set_password("123")
                                teacher_obj.save()
                            # todo 新建课程
                            for week in range(week_start, week_num + 1):
                                # try:
                                #     schedule = Schedule.objects.get(week=week, weekday=weekday, order=order)
                                # except Schedule.DoesNotExist:
                                #
                                #     schedule = Schedule.objects.create(week=week, weekday=weekday, order=order)

                                time_str = sheet.cell_value(order_indexes[i], 2).split('--')
                                time_list = []  # 上课时间，下课时间
                                for time in time_str:
                                    time=time.replace(" ","")
                                    time=time.replace("：", ":")
                                    time2datetime = datetime.datetime.strptime(time, '%H:%M')  # 文字转datetime
                                    # datetime 转 timedelta
                                    timediff = datetime.timedelta(weeks=week - 1, days=weekday - 1,
                                                                  hours=time2datetime.hour,
                                                                  minutes=time2datetime.minute)
                                    # 实际时间=第一周时间+timedelta
                                    time_list.append(utc2local(first_week_date + timediff))


                                try:
                                    course = Course.objects.get(teacher_id=teacher_obj,week=week, weekday=weekday, order=order)
                                    course.name = course_name
                                    course.teacher_id = teacher_obj
                                    course.class_id = class_obj
                                    course.start_time = time_list[0]
                                    course.end_time = time_list[1]
                                    course.save()
                                except Course.DoesNotExist:
                                    Course.objects.create(name=course_name, teacher_id=teacher_obj, class_id=class_obj,
                                                          week=week, weekday=weekday, order=order,
                                                          start_time=time_list[0], end_time=time_list[1])
        except Exception as e:
            raise e
            return 0

    return 1

# def test():
#     import sys
#     import os
#     import django
#     # 这两行很重要，用来寻找项目根目录，os.path.dirname要写多少个根据要运行的python文件到根目录的层数决定
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     sys.path.append(BASE_DIR)
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
#     django.setup()
#     from schools.models import School
#     print(School.objects.all().values('name'))


#
# if __name__ == '__main__':
#
#     test()
# from utils.insertdata import test
# test()
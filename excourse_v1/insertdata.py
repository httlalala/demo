import time

from django.db import transaction

from users.models import User
from applications.models import Application
from classes.models import Class
from schools.models import School
from courses.models import Course, CourseTime

'''

'''

def zhx():
    import xlrd
    import json
    book = xlrd.open_workbook('xxxx.xls')
    sheet_names = book.sheet_names()

    for sheet_name in sheet_names:  # 遍历每一个表
        sheet = book.sheet_by_name(sheet_name)
        for row in range(sheet.nrows):
            rowData = sheet.row_values(row)
            # todo 从rowData 提取出来想要的东西，组织称字典 MyDict
            # 可能用到的方法：sheet.row_values(i)，sheet.col_values(i)，sheet.cell_value(i,j)
            MyDict = {'Name':rowData[0],'Level':rowData[1]}
            # todo 写json
            filename = "第%s行的数据.json" % str(row+1)  # 可以用格式化字符串自己定义
            f=open(filename,mode='w',encoding='utf-8')
            json.dump(MyDict,f,indent=4,ensure_ascii=False)



def generateData():
    mapdict = {
        '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9
    }

    # School.objects.create(id=1, province="河北省", city="石家庄市", region="栾城区", address="人民大街111号", name="实验小学")
    try:
        school = School.objects.get(id=1)
    except School.DoesNotExist:
        return

    import xlrd
    from tqdm import tqdm

    order_indexes = [4, 5, 7, 9, 10, 11]
    weekday_indexes = [3, 4, 5, 6, 7]

    book = xlrd.open_workbook('course.xls')
    class_list = book.sheet_names()
    for class_name in tqdm(class_list):
        sheet = book.sheet_by_name(class_name)
        # todo 拿到 学校id 和 周次
        week = 1
        # todo 拿到 年级 和 班号
        grade = mapdict.get(class_name[0], None)
        class_number = int(class_name[1])
        # todo 如果班级不存在  那么新建班级
        try:
            class_obj = Class.objects.get(school_id=school, grade=grade, class_number=class_number)
        except Class.DoesNotExist:
            class_obj = Class.objects.create(school_id=school, grade=grade, class_number=class_number)

        for j in range(len(weekday_indexes)):
            for i in range(len(order_indexes)):
                # todo 拿到这节课的  教师名字  课程名  星期 节次
                course = sheet.cell_value(order_indexes[i], weekday_indexes[j])
                if course.strip() != '':
                    weekday = j+1
                    order = i+1
                    course_name, teacher_name = course.split('\n')[0],course.split('\n')[1]
                    teacher_name = teacher_name.replace('(', '')
                    teacher_name = teacher_name.replace(')', '')
                    # todo 如果教师不存在  那么新建教师
                    try:
                        teacher_obj = User.objects.get(school_id=school, username=teacher_name)
                    except User.DoesNotExist:
                        teacher_obj = User.objects.create(phone='111111%s' % str(time.time())[-5:], school_id=school,username=teacher_name)
                        teacher_obj.set_password("123")
                        teacher_obj.save()
                    # todo 新建课程
                    # try:
                    #     course_time = CourseTime.objects.get(week=week,weekday=weekday,order=order)
                    # except CourseTime.DoesNotExist:
                    #     course_time = CourseTime.objects.create(week=week, weekday=weekday, order=order)
                    try:
                        Course.objects.get(name=course_name, teacher_id=teacher_obj, class_id=class_obj, week=week,weekday=weekday, order=order)
                    except Course.DoesNotExist:
                        Course.objects.create(name=course_name, teacher_id=teacher_obj, class_id=class_obj,week=week,weekday=weekday,order=order)


def updatephone():
    from tqdm import tqdm
    qs = User.objects.all()
    for user in tqdm(qs):
        user.phone = '111111%s' % str(time.time())[-5:]
        user.save()

def updatepassword():
    from tqdm import tqdm
    qs = User.objects.all()
    for user in tqdm(qs):
        user.set_password("123")
        user.save()

def updatecourse_time():
    from tqdm import tqdm
    qs = Course.objects.all()
    for course in tqdm(qs):
        try:
            course_time = CourseTime.objects.get(week=course.week,weekday=course.weekday,order=course.order)
        except CourseTime.DoesNotExist:
            course_time = CourseTime.objects.create(week=course.week, weekday=course.weekday, order=course.order)
        course.course_time_id = course_time



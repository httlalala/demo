import datetime
from schools.models import School

def utc2local(utctime):
    localtime = utctime.replace(tzinfo=None) + datetime.timedelta(hours=8)
    return localtime

def date2week(school_id,date):
    first_week_time = utc2local(School.objects.get(id=school_id).first_week_date)

    try:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return -1
    if date<first_week_time:
        return -1
    datediff = (date.date() - first_week_time.date()).days
    return (datediff//7 + 1)


def week2date(school_id,week):
    first_week_time = utc2local(School.objects.get(id=school_id).first_week_date)
    week_num = School.objects.get(id=school_id).week_num

    week = 1 if week<1 else week
    week = week_num if week>week_num else week

    date = first_week_time.date() + datetime.timedelta(weeks=week-1)

    return date.__str__()
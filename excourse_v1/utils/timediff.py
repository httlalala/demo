import datetime


def utf2local(utctime):
    localtime = utctime.replace(tzinfo=None) + datetime.timedelta(hours=8)
    return localtime
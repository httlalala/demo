import json
from quopri import quote
from urllib import request, parse
from django.conf import settings

def sendTemplateSMS(name,code,mobile):
    if not settings.MESSAGE_CAN_USE:
        return {'stat':100}
    uid = 'rochelimit'
    pwd = 'ce6d5daef224ee974b6a4502995ef226'
    content = quote('你好！%s,您的验证码：%s。如非本人操作，可不用理会！【智能调课系统】'%(name,code),'utf-8')
    # 拼接URL
    url = 'http://api.sms.cn/sms/?ac=send&uid='+uid+'&pwd='+pwd+'&mobile='+mobile+'&content='+content
    # 生成auth
    try:
        res = request.urlopen(url)
        data = res.read()
        res.close()
        return eval(data)
    except Exception as error:
        return {'stat':403,'msg':'发送失败'}

def substitutionComplete(teacher_name,manager_name,mobile):
    if not settings.MESSAGE_CAN_USE:
        return {'stat':100}
    uid = 'rochelimit'
    pwd = 'ce6d5daef224ee974b6a4502995ef226'
    content={"t1":teacher_name,"t2":manager_name}
    content = parse.quote(json.dumps(content))
    # 拼接URL
    url = 'http://api.sms.cn/sms/?ac=send&uid='+uid+'&pwd='+pwd+'&template=557447'+'&mobile='+mobile+'&content='+content
    # 生成auth
    try:
        res = request.urlopen(url)
        data = res.read()
        res.close()
        return eval(data)
    except Exception as error:
        print(error)
        return {'stat': 403, 'msg': '发送失败'}


def substitutionTarget(applicant_name,manager_name,target_name,mobile):
    if not settings.MESSAGE_CAN_USE:
        return {'stat':100}
    uid = 'rochelimit'
    pwd = 'ce6d5daef224ee974b6a4502995ef226'
    content = {"t1": target_name, "t2": applicant_name, "admin": manager_name}
    content = parse.quote(json.dumps(content))
    # 拼接URL
    url = 'http://api.sms.cn/sms/?ac=send&uid=' + uid + '&pwd=' + pwd + '&template=551406' + '&mobile=' + mobile + '&content=' + content
    # 生成auth
    try:
        res = request.urlopen(url)
        data = res.read()
        res.close()
        return eval(data)
    except Exception as error:
        print(error)
        return {'stat': 403, 'msg': '发送失败'}


def substitutionApplicant(applicant_name,manager_name,mobile):
    if not settings.MESSAGE_CAN_USE:
        return {'stat':100}
    uid = 'rochelimit'
    pwd = 'ce6d5daef224ee974b6a4502995ef226'
    content={"t1":applicant_name,"t2":manager_name}
    content = parse.quote(json.dumps(content))
    # 拼接URL
    url = 'http://api.sms.cn/sms/?ac=send&uid='+uid+'&pwd='+pwd+'&template=557447'+'&mobile='+mobile+'&content='+content
    # 生成auth
    try:
        res = request.urlopen(url)
        data = res.read()
        res.close()
        return eval(data)
    except Exception as error:
        print(error)
        return {'stat': 403, 'msg': '发送失败'}


def exchangeApplicant(applicant_name,target_name,mobile):
    if not settings.MESSAGE_CAN_USE:
        return {'stat':100}
    uid = 'rochelimit'
    pwd = 'ce6d5daef224ee974b6a4502995ef226'
    content={"t1":applicant_name,"t2":target_name}
    content = parse.quote(json.dumps(content))
    # 拼接URL
    url = 'http://api.sms.cn/sms/?ac=send&uid='+uid+'&pwd='+pwd+'&template=552758'+'&mobile='+mobile+'&content='+content
    # 生成auth
    try:
        res = request.urlopen(url)
        data = res.read()
        res.close()
        return eval(data)
    except Exception as error:
        print(error)
        return {'stat': 403, 'msg': '发送失败'}



#coding:utf-8
import requests
import base64
import json
import redis
from requests.auth import HTTPBasicAuth
from celery import Celery
from flask import Flask,jsonify
from celery.schedules import crontab
from datetime import timedelta
from os import sys,path
from make_celery import make_celery
from flask_script import Manager 

#每天24h,每小时发送6次
TOTAL = 144

#每次检查间隔时间
TIME_EVERY_CHECK=10

#set i
i = 0

#redis链接池
pool01 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)
pool02 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2)
pool03 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=3)
pool04 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=4)
pool05 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=5)
pool06 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=6)
pool07 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=7)
pool08 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=8)
pool09 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=9)
pool10 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=10)
pool11 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=11)
pool12 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=12)
pool13 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=13)
pool14 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=14)
pool15 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=15)
pool16 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=16)
pool17 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=17)
pool18 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=18)
pool19 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=19)
pool21 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=21)
pool22 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=22)
pool23 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=23)
pool24 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=24)

r01 = redis.StrictRedis(connection_pool=pool01)
r02 = redis.StrictRedis(connection_pool=pool02)
r03 = redis.StrictRedis(connection_pool=pool03)
r04 = redis.StrictRedis(connection_pool=pool04)
r05 = redis.StrictRedis(connection_pool=pool05)
r06 = redis.StrictRedis(connection_pool=pool06)
r07 = redis.StrictRedis(connection_pool=pool07)
r08 = redis.StrictRedis(connection_pool=pool08)
r09 = redis.StrictRedis(connection_pool=pool09)
r10 = redis.StrictRedis(connection_pool=pool10)
r11 = redis.StrictRedis(connection_pool=pool11)
r12 = redis.StrictRedis(connection_pool=pool12)
r13 = redis.StrictRedis(connection_pool=pool13)
r14 = redis.StrictRedis(connection_pool=pool14)
r15 = redis.StrictRedis(connection_pool=pool15)
r16 = redis.StrictRedis(connection_pool=pool16)
r17 = redis.StrictRedis(connection_pool=pool17)
r18 = redis.StrictRedis(connection_pool=pool18)
r19 = redis.StrictRedis(connection_pool=pool19)
r21 = redis.StrictRedis(connection_pool=pool21)
r22 = redis.StrictRedis(connection_pool=pool22)
r23 = redis.StrictRedis(connection_pool=pool23)
r24 = redis.StrictRedis(connection_pool=pool24)

#信息门户头部信息:貌似有两套头部信息...
login_info_header = {
    'Bigipserverpool_Jwc_Xk': '139503808.20480.0000',
    'Sid': '2014210761',
    'Jsessionid': 'B6A6DF5C48AB4AD4C4001572D2611809',
    'Authorization': "Basic Base64(sid:pwd)"
}

usrPass = "2016210942:130395"
b64Val = base64.b64encode(usrPass)



#图书馆头部信息
Passlib ="2016210942:123456"
b64Vallib = base64.b64encode(Passlib)

#管理员头部信息
adminPass = "muxistudio@qq.com:<!--muxi-->"
b64admin = base64.b64encode(adminPass)

#初始化APP
app = Flask(__name__)

#URLS
url01 = "https://ccnubox.muxixyz.com/api/info/login/"
url02 = "https://ccnubox.muxixyz.com/api/lib/login/"
url03 = "https://ccnubox.muxixyz.com/api/lib/search/?keyword=计算机&page=1"
url04 = "https://ccnubox.muxixyz.com/api/lib/?id=0000475103"
url05 = "https://ccnubox.muxixyz.com/api/lib/me/"
url06 = "https://ccnubox.muxixyz.com/api/table/"
url07 = "https://ccnubox.muxixyz.com/api/table/"
url08 = "https://ccnubox.muxixyz.com/api/ios/table/"
url09 = "https://ccnubox.muxixyz.com/api/table/5/"
url10 = "https://ccnubox.muxixyz.com/api/ios/table/5/"
url11 = "https://ccnubox.muxixyz.com/api/ele/"
url12 = "https://ccnubox.muxixyz.com/api/ele/"
url13 = "https://grade.muxixyz.com/api/grade/search/?xnm=2016&xqm=3/"
url14 = "https://ccnubox.muxixyz.com/api/apartment/"
url15 = "https://ccnubox.muxixyz.com/api/site/"
url16 = "https://ccnubox.muxixyz.com/api/info/"
url17 = "https://ccnubox.muxixyz.com/api/banner/"
url18 = "https://ccnubox.muxixyz.com/api/ios/banner/"
url19 = "https://ccnubox.muxixyz.com/api/calendar/"
url20 = "https://ccnubox.muxixyz.com/api/ios/calendar/"
url21 = "https://ccnubox.muxixyz.com/api/start/"
url22 = "https://ccnubox.muxixyz.com/api/feedback/"
url23 = "https://ccnubox.muxixyz.com/api/ios/config/"
url24 = "https://ccnubox.muxixyz.com/api/product/"

#以便返回汉字
app.config['JSON_AS_ASCII'] = False

#配置Celery
app.config.update(
    CELERY_BROKER_URL='redis://127.0.0.1:6379',
    CELERY_RESULT_BACKEND='redis://127.0.0.1:6379/0',
    #Timezone
    CELERY_TIMEZONE = 'Asia/Shanghai',

    CELERYBEAT_SCHEDULE = {
        'main':{
            'task':'main',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK)
        }
    })

#初始化Celery
celery = make_celery(app)

#tasks

#信息门户登录
def login_xinximenhu(i):
    resp01 = requests.get("https://ccnubox.muxixyz.com/api/info/login/",
                            headers = {"Authorization": "Basic %s" %b64Val})
    statu01 = resp01.status_code
    r01.set(i,statu01)
 
#登录图书馆 
def login_lib(i):
    resp02= requests.get("https://ccnubox.muxixyz.com/api/lib/login/",
                            headers = {"Authorization": "Basic %s" %b64Vallib})
    statu02 = resp02.status_code
    r02.set(i,statu02)

#查询图书
def find_book(i):
    resp03 = requests.get("https://ccnubox.muxixyz.com/api/lib/search/?keyword=计算机&page=1")
    statu03 = resp03.status_code
    r03.set(i,statu03)

#图书详情
def book_info(i):
    resp04 = requests.get("https://ccnubox.muxixyz.com/api/lib/?id=0000475103")
    statu04 = resp04.status_code
    r04.set(i,statu04)

#我的图书馆
def my_lib(i):
    resp05 = requests.get("https://ccnubox.muxixyz.com/api/lib/me/",
                            headers = {"Authorization": "Basic %s" % b64Vallib})
    statu05 = resp05.status_code
    r05.set(i,statu05)

#查询课表
def inqu_table(i):
    resp06=requests.get("https://ccnubox.muxixyz.com/api/table/",
                            headers = {"Authorization":"Basic %s" %b64Val})
    statu06 = resp06.status_code
    r06.set(i,statu06)


#添加课程
def add_class(i):
    post_data={
            "course":"test",
            "teacher":"test",
            "weeks":"1,2,3,4",
            "day":"星期1",
            "start":"1",
            "during":"1",
            "place":"9-11",
            "remind":False
    }
    resp07=requests.post("https://ccnubox.muxixyz.com/api/table/",
                            json = post_data,
                            headers = login_info_header)
    statu07 = resp07.status_code
    r07.set(i,statu07)

#添加课程 For IOS
def add_class_ios(i):
    post_data={
            "course":"test",
            "teacher":"test",
            "weeks":"1,2,3,4",
            "day":"星期1",
            "start":"3",
            "during":"2",
            "place":"9-21",
            "remind":False
        }
    resp08=requests.post("https://ccnubox.muxixyz.com/api/ios/table/",
                            json =  post_data,
                            headers = {"Authorization":"Basic %s" %b64Val} )
    statu08 = resp08.status_code
    r08.set(i,statu08)

#删除课程 ID 为课程ID
def delete_class(i):
    resp09 = requests.delete("https://ccnubox.muxixyz.com/api/table/5/",
                                        headers = login_info_header)
    statu09=resp09.status_code
    r09.set(i,statu09)

#编辑课表
def edit_table(i):
    post_data={
            "course":"test",
            "teacher":"test",
            "weeks":"1,2,3,4",
            "day":"星期一",
            "start":"3",
            "during":"2",
            "place":"9-11",
            "remind":False
    }    
    resp10 = requests.put( "https://ccnubox.muxixyz.com/api/table/5/",
                                        json = post_data ,
                                        headers = {"Authorization":"Basic %s" %b64Val} )

    statu10=resp10.status_code
    r10.set(i,statu10)

#空调电费查询
def ele_air(i):
    post_data = {
        "dor":"东1-101",
        "type": "air"
    }
    resp11 = requests.post("https://ccnubox.muxixyz.com/api/ele/",json = post_data)
    statu11=resp11.status_code
    r11.set(i,statu11)    

#照明电费查询
def ele_light(i):
    post_data = {
        "dor":"东1-101",
        "type": "light"
        }
    resp12 = requests.post("https://ccnubox.muxixyz.com/api/ele/",json = post_data  )
    statu12=resp12.status_code
    r12.set(i,statu12)

#成绩查询
def grade_total(i):
    resp13 = requests.get("https://grade.muxixyz.com//api/grade/?xnm=2015&xqm=3",
                            headers = login_info_header)
    
    statu13=resp13.status_code
    r13.set(i,statu13)

#平时成绩查询
def grade_detail(i):
    pass;

#部门信息
def apartment(i):
    resp14 = requests.get("https://ccnubox.muxixyz.com/api/apartment/")
    statu14 = resp14.status_code
    r14.set(i,statu14)

#常用网站
def site(i):
    resp15 = requests.get("https://ccnubox.muxixyz.com/api/site/")
    statu15 = resp15.status_code
    r15.set(i,statu15)

#通知公告
def info(i):
    resp16 = requests.get("https://ccnubox.muxixyz.com/api/info/")
    statu16 = resp16.status_code
    r16.set(i,statu16)

#Banner获取
def banner(i):
    resp17 = requests.get("https://ccnubox.muxixyz.com/api/banner/")
    statu17 = resp17.status_code
    r17.set(i,statu17)

#Banner获取IOS
def banner_ios(i):
    resp18 = requests.get("https://ccnubox.muxixyz.com/api/ios/banner/") 
    statu18 = resp18.status_code
    r18.set(i,statu18)

#校历
def calendar(i):
    resp19 = requests.get("https://ccnubox.muxixyz.com/api/calendar/")
    statu19 = resp19.status_code
    r19.set(i,statu19)

#闪屏
def start(i):
    resp21 = requests.get("https://ccnubox.muxixyz.com/api/start/")
    statu21 = resp21.status_code
    r21.set(i,statu21)


#IOS用户反馈
def feedback(i):
    resp22 = requests.get("https://ccnubox.muxixyz.com/api/feedbacks/",
                            headers = {"Authorization":"Basic %s" %b64admin})
    statu22 = resp22.status_code
    r22.set(i,statu22)
    
#获取IOS json数据
def config_ios(i):
    resp23 = requests.get("https://ccnubox.muxixyz.com/api/ios/config/")
    statu23 = resp23.status_code
    r23.set(i,statu23)

#木犀产品展示
def product(i):
    resp24 = requests.get("https://ccnubox.muxixyz.com/api/product/")
    statu24 = resp24.status_code
    r24.set(i,statu24)

@celery.task(name = 'main')
def main():
    global i
    
    login_xinximenhu(i)
    login_lib(i)
    find_book(i)
    book_info(i)
    my_lib(i)
    inqu_table(i)
    add_class(i)
    add_class_ios(i)
    edit_table(i)
    delete_class(i)
    ele_air(i)
    ele_light(i)
    grade_total(i)
    apartment(i)
    site(i)
    info(i)
    banner(i)
    banner_ios(i)
    calendar(i)
    start(i)
    feedback(i)
    config_ios(i)
    product(i)
    
    if i<TOTAL-1:
        i = i + 1
    elif i==TOTAL-1:
        i = 0
    

@app.route("/")
def index():
    return jsonify({
            "login_xinximenhu":[r01.get(k) for k in range(144)],
            "login_lib":[r02.get(k) for k in range(144)],
            "inquire_book":[r03.get(k) for k in range(144)],
            "book's_infomation":[r04.get(k) for k in range(144)],
            "my_lib":[r05.get(k) for k in range(144)],
            "inquire_classes_table":[r06.get(k) for k in range(144)],
            "add_class":[r07.get(k) for k in range(144)],
            "add_class_for_IOS":[r08.get(k) for k in range(144)],
            "delete_class":[r09.get(k) for k in range(144)],
            "edit_class":[r10.get(k) for k in range(144)],
            "air_electricity":[r11.get(k) for k in range(144)],
            "light_electricity":[r12.get(k) for k in range(144)],
            "inquire_grades":[r13.get(k) for k in range(144)],
            "apartment_infomation":[r14.get(k) for k in range(144)],
            "useful_websites":[r15.get(k) for k in range(144)],
            "announcement":[r16.get(k) for k in range(144)],
            "get_Banner":[r17.get(k) for k in range(144)],
            "get_Banner_for_IOS":[r18.get(k) for k in range(144)],
            "calendar":[r19.get(k) for k in range(144)],
            "start":[r21.get(k) for k in range(144)],
            "feedback_for_IOS":[r22.get(k) for k in range(144)],
            "get_json_for_IOS":[r23.get(k) for k in range(144)],
            "muxi's_products":[r24.get(k) for k in range(144)],
            })
if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)

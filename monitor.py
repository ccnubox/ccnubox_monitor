#coding:utf-8
from __future__ import absolute_import
import requests
import base64
import redis
from requests.auth import HTTPBasicAuth
from celery import Celery
from flask import Flask,jsonify
from celery.schedules import crontab
from datetime import timedelta
from os import sys,path
from make_celery import make_celery
from flask_script import Manager 

#每次检查间隔时间
TIME_EVERY_CHECK=10

#redis链接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)
r = redis.StrictRedis(connection_pool=pool)

#信息门户头部信息
usrPass = "2016210942:130395"
b64Val = base64.b64encode(usrPass)

#图书馆头部信息
Passlib ="2016210942:123456"
b64Vallib = base64.b64encode(Passlib)

#初始化APP
app = Flask(__name__)

#URLS
url01="https://ccnubox.muxixyz.com/api/info/login/"
url02="https://ccnubox.muxixyz.com/api/lib/login/"
url03="https://ccnubox.muxixyz.com/api/lib/search/?keyword=计算机&page=1/"
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


#配置
app.config.update(
    
    CELERY_BROKER_URL='redis://127.0.0.1:6379',
    CELERY_RESULT_BACKEND='redis://127.0.0.1:6379/0',
    #Timezone
    CELERY_TIMEZONE = 'Asia/Shanghai',
    #import
    #CELERY_IMPORTS = (
    #    'celery_app.tasks'
    #)
    #
    #schedules

    CELERYBEAT_SCHEDULE = {
        'login_xinximenhu':{
            'task': 'login_xinximenhu',
            'schedule': timedelta(seconds = TIME_EVERY_CHECK),
        },
        'login_library':{
            'task':'login_lib',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'find_books':{
            'task':'find_book',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'booksinfo':{
            'task':'book_info',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'mylib':{
            'task':'my_lib',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'inqu_table':{
            'task':'inqu_table',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'add_classes':{
            'task':'add_class',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'add_classes_ios':{
            'task':'add_class_ios',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'delete_class':{
            'task':'delete_class',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
	    'edit_table':{
            'task':'edit_table',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'ele_air':{
            'task':'ele_air',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'ele_light':{
            'task':'ele_light',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'grade_total':{
            'task':'grade_total',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'grade_detail':{
            'task':'grade_detail',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'apartment':{
            'task':'apartment',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'site':{
            'task':'site',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'info':{
            'task':'info',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'banner':{
            'task':'banner',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'banner_ios':{
            'task':'banner_ios',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'calendar':{
            'task':'calendar',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'calendar_ios':{
        'task':'calendar_ios',
        'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'start':{
            'task':'start',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
	    'product':{
            'task':'product',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
	    },
        'feedback':{
            'task':'feedback',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'config_ios':{
            'task':'config_ios',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
    })

celery = make_celery(app)

#tasks

#信息门户登录
@celery.task(name='login_xinximenhu')
def login_xinximenhu():
    resp01 = requests.get("https://ccnubox.muxixyz.com/api/info/login/",\
                            headers = {"Authorization": "Basic %s" %b64Val})
    statu01 = resp01.status_code
    r.set(url01,statu01)
 
#登录图书馆 
@celery.task(name='login_lib')
def login_lib():
    resp02= requests.get("https://ccnubox.muxixyz.com/api/lib/login/",\
                            headers = {"Authorization": "Basic %s" %b64Vallib})
    statu02 = resp02.status_code
    r.set(url02,statu02)

#查询图书
@celery.task(name='find_book')
def find_book():
    resp03 = requests.get("https://ccnubox.muxixyz.com/api/lib/search/?keyword=计算机&page=1/")
    statu03 = resp03.status_code
    r.set(url03,statu03)

#图书详情
@celery.task(name='book_info')
def book_info():
    resp04 = requests.get("https://ccnubox.muxixyz.com/api/lib/?id=0000475103")
    statu04 = resp04.status_code
    r.set(url04,statu04)

#我的图书馆
@celery.task(name='my_lib')
def my_lib():
    resp05 = requests.get("https://ccnubox.muxixyz.com/api/lib/me/",\
                            headers = {"Authorization": "Basic %s" % b64Vallib})
    statu05 = resp05.status_code
    r.set(url05,statu05)

#查询课表
@celery.task(name='inqu_table')
def inqu_table():
    resp06=requests.get("https://ccnubox.muxixyz.com/api/table/",\
                            headers = {"Authorization":"Basic %s" %b64Val})
    statu06 = resp06.status_code
    r.set(url06,statu06)


#添加课程
@celery.task(name='add_class')
def add_class():
    post_data={
            "id":"1",
            "course":"爱情心理学",
            "teacher":"余海军",
            "weeks":"1,2,3,4",
            "day":"7",
            "start":"1",
            "during":"1",
            "place":"9-11",
            "remind":0
    }
    resp07=requests.post("https://ccnubox.muxixyz.com/api/table/",\
                            params = post_data,\
                            headers = {"Authorization":"Basic %s" %b64Val} )
    statu07 = resp07.status_code
    r.set(url07,statu07)

#添加课程 For IOS
@celery.task(name='add_class_ios')
def add_class_ios():
    post_data={
            "course":"爱情心理学",
            "teacher":"余海军",
            "weeks":"1,2,3,4",
            "day":"7",
            "start":"1",
            "during":"1",
            "place":"9-11",
            "remind":0
        }
    resp08=requests.post("https://ccnubox.muxixyz.com/api/ios/table/",\
                            params = post_data,\
                            headers = {"Authorization":"Basic %s" %b64Val} )
    statu08 = resp08.status_code
    r.set(url08,statu08)

#删除课程 ID 为课程ID
@celery.task(name='delete_class')
def delete_class():
    resp09 = requests.delete("https://ccnubox.muxixyz.com/api/table/5/")
    statu09=resp09.status_code
    r.set(url09,statu09)

#编辑课表
@celery.task(name='edit_table')
def edit_table():
    post_data={
            "course":"爱情心理学",
            "teacher":"余海军",
            "weeks":"1,2,3,4",
            "day":"6",
            "start":"6",
            "during":"2",
            "place":"9-11",
            "remind":0
    }    
    resp10 = requests.put( "https://ccnubox.muxixyz.com/api/ios/table/5/",\
                                        params = post_data ,\
                                        headers = {"Authorization":"Basic %s" %b64Val} )

    statu10=resp10.status_code
    r.set(url10,statu10)

#空调电费查询
@celery.task(name='ele_air')
def ele_air():
    post_data = {
        "dor":"东1-101",
        "type": "air"
    }
    resp11 = requests.post("https://ccnubox.muxixyz.com/api/ele/",\
                                params = post_data)
    statu11=resp11.status_code
    r.set(url11,statu11)    

#照明电费查询
@celery.task(name='ele_light')
def ele_light():
    post_data = {
        "dor":"东1-101",
        "type": "light"
        }
    resp12 = requests.post(   "https://ccnubox.muxixyz.com/api/ele/",\
                                        params = post_data  )
    statu12=resp12.status_code
    r.set(url12,statu12)

#成绩查询
@celery.task(name='grade_total')
def grade_total():
    resp13 = requests.get("https://grade.muxixyz.com/api/grade/search/?xnm=2016&xqm=3/",\
                            headers = {"Authorization":"Basic %s" %b64Val} )
    
    statu13=resp13.status_code
    r.set(url13,statu13)


#平时成绩查询
@celery.task(name='grade_detail')
def grade_detail():
    pass;

#部门信息
@celery.task(name='apartment')
def apartment():
    resp14 = requests.get("https://ccnubox.muxixyz.com/api/apartment/")
    statu14 = resp14.status_code
    r.set(url14,statu14)

#常用网站
@celery.task(name='site')
def site():
    resp15 = requests.get("https://ccnubox.muxixyz.com/api/site/")
    statu15 = resp15.status_code
    r.set(url15,statu15)

#通知公告
@celery.task(name='info')
def info():
    resp16 = requests.get("https://ccnubox.muxixyz.com/api/info/")
    statu16 = resp16.status_code
    r.set(url16,statu16)

#Banner获取
@celery.task(name='banner')
def banner():
    resp17 = requests.get("https://ccnubox.muxixyz.com/api/banner/")
    statu17 = resp17.status_code
    r.set(url17,statu17)

#Banner获取IOS
@celery.task(name='banner_ios')
def banner_ios():
    resp18 = requests.get("https://ccnubox.muxixyz.com/api/ios/banner/") 
    statu18 = resp18.status_code
    r.set(url18,statu18)

#校历
@celery.task(name='calendar')
def calendar():
    resp19 = requests.get("https://ccnubox.muxixyz.com/api/calendar/")
    statu19 = resp19.status_code
    r.set(url19,statu19)

#校历IOS
@celery.task(name='calendar_ios')
def calendar_ios():
    resp20 = requests.get("https://ccnubox.muxixyz.com/api/ios/calendar/")
    statu20 = resp20.status_code
    r.set(url20,statu20)

#闪屏
@celery.task(name='start')
def start():
    resp21 = requests.get("https://ccnubox.muxixyz.com/api/start/")
    statu21 = resp21.status_code
    r.set(url21,statu21)


#IOS用户反馈
@celery.task(name='feedback')
def feedback():
    resp22 = requests.get("https://ccnubox.muxixyz.com/api/feedback/")
    statu22 = resp22.status_code
    r.set(url22,statu22)
    
#获取IOS json数据
@celery.task(name='config_ios')
def config_ios():
    resp23 = requests.get("https://ccnubox.muxixyz.com/api/ios/config/")
    statu23 = resp23.status_code
    r.set(url23,statu23)

#木犀产品展示
@celery.task(name='product')
def product():
    resp24 = requests.get("https://ccnubox.muxixyz.com/api/product/")
    statu24 = resp24.status_code
    r.set(url24,statu24)

@app.route("/")
def index():
   return jsonify({
            url01:r.get(url01),
            url02:r.get(url02),
            url03:r.get(url03),
            url04:r.get(url04),
            url05:r.get(url05),
            url06:r.get(url06),
            url07:r.get(url07),
            url08:r.get(url08),
            url09:r.get(url09),
            url10:r.get(url10),
            url11:r.get(url11),
            url12:r.get(url12),
            url13:r.get(url13),
            url14:r.get(url14),
            url15:r.get(url15),
            url16:r.get(url16),
            url17:r.get(url17),
            url18:r.get(url18),
            url19:r.get(url19),
            url20:r.get(url20),
            url21:r.get(url21),
            url22:r.get(url22),
            url23:r.get(url23),
            url24:r.get(url24),
            })

if __name__ =='__main__':
    app.run(debug=True)

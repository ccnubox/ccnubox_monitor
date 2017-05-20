#coding:utf-8
import requests
import base64
import redis
import json
from flask import jsonify
from requests.auth import HTTPBasicAuth

#pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
#r = redis.StrictRedis(connection_pool=pool)

login_info_header = {
    'Bigipserverpool_Jwc_Xk':'139503808.20480.0000',
    'Sid':'2014210761',
    'Jsessionid':'B6A6DF5C48AB4AD4C4001572D2611809',
    'Authorization':"Basic Base64(sid:pwd)"
}

usrPass = "2016210942:130395"
b64Val = base64.b64encode(usrPass)

'''
resp16 = requests.get("https://ccnubox.muxixyz.com/api/webview_info/")
statu16 = resp16.status_code
print statu16
'''

'''
resp13 = requests.get("https://grade.muxixyz.com//api/grade/?xnm=2015&xqm=3/",
                            headers = login_info_header)
    
statu13=resp13.status_code
print statu13

'''



'''
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
                            headers = {"Authorization":"Basic %s" %b64Val})
statu08 = resp08.status_code
print statu08
'''

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
#print resp07.text
#print type(resp07.text)
json_data = resp07.json()
#print json_data
print type(json_data)
global class_id 
class_id = json_data["id"]
#print class_id

#删除课程 ID 为课程ID

resp09 = requests.delete("https://ccnubox.muxixyz.com/api/table/"+str(class_id)+"/",
                                headers = login_info_header )
statu09=resp09.status_code
print statu09



'''
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
print resp07.text
'''
#usrPass = "2016210942:130395"
#b64Val = base64.b64encode(usrPass)

#r = requests.get("https://ccnubox.muxixyz.com/api/table/",headers = {"Authorization":"Basic %s" %b64Val} )

#print r.text

'''
json = jsonify({
        "登录信息门户":"1",
        "木犀产品展示":"2",
})

'''

'''
post_data={
            "course":"test",
            "teacher":"test",
            "weeks":"1,2,3,4",
            "day":"星期1",
            "start":"3",
            "during":"2",
            "place":"9-21",
            "remind": False
        }
resp08=requests.post("https://ccnubox.muxixyz.com/api/ios/table/",\
                            params = post_data,\
                            headers = {"Authorization":"Basic %s" %b64Val} )
print resp08.text
print resp08.status_code
'''
'''
resp13 = requests.get("https://grade.muxixyz.com/api/grade/search/?xnm=2016&xqm=3/",\
                            headers = {"Authorization":"Basic %s" %b64Val} )    
print resp13.text
'''
'''
post_data={
        "course":"爱情心理学",
        "teacher":"余海军",
        "weeks":"1,2,3,4",
        "day":"5",
        "start":"8",
        "during":"2",
        "place":"9-11",
        "remind":0
}

add_classes_resp = requests.post( "https://ccnubox.muxixyz.com/api/ios/table/",params = post_data,headers = {"Authorization":"Basic %s" %b64Val})

r.set("https://123",add_classes_resp.status_code)
url = "https://123"
r.set("abcd","1111111")
r.set(url,"8888")
print(r.get(url))
print(r.get("abcd"))
'''

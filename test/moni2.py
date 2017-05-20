#coding:utf-8
import requests
from pprint import pprint
info_login_url = "http://portal.ccnu.edu.cn/loginAction.do"
link_url = "http://portal.ccnu.edu.cn/roamingAction.do?appId=XK"
login_ticket_url = "http://122.204.187.6/xtgl/login_tickitLogin.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
}

post_data = {
	'userName': 2016210942, 
	'userPass': 130395
}

_cookie_jar = None

s = requests.Session()
r = s.post(info_login_url,data = post_data)
if r.text.split('"')[1] == 'index_jg.jsp':
	r_second = s.get(link_url,timeout = 4)
	r_third = s.get(login_ticket_url,timeout = 4)
	ret = s.__dict__
	cookies = ret['cookies']


	_cookie_jar = s.__dict__.get('_cookie_jar')
	
	pprint(s.__dict__)
	print('\n\n\n\n')
	

	print cookies.keys()
	


	
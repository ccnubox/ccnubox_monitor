启动：
1,flask project: python manage.py runserver
2,redis: redis-server --port 6379
3,celery(main process): celery worker --app xxx.celery --loglevel=info
4,celery(beat): celery beat --app xxx.celery --loglevel=info
***
POST：

NONE
***
RETURN:

    {
    
    "https://ccnubox.muxixyz.com/api/apartment/": "200",
    "https://ccnubox.muxixyz.com/api/banner/": "200",
    "https://ccnubox.muxixyz.com/api/calendar/": "200", 
    "https://ccnubox.muxixyz.com/api/ele/": "500", 
    "https://ccnubox.muxixyz.com/api/feedback/": "500", 
    "https://ccnubox.muxixyz.com/api/info/": "200", 
    "https://ccnubox.muxixyz.com/api/info/login/": "200", 
    "https://ccnubox.muxixyz.com/api/ios/banner/": "200", 
    "https://ccnubox.muxixyz.com/api/ios/calendar/": "404", 
    "https://ccnubox.muxixyz.com/api/ios/config/": "200", 
    "https://ccnubox.muxixyz.com/api/ios/table/": "500", 
    "https://ccnubox.muxixyz.com/api/ios/table/5/": "404", 
    "https://ccnubox.muxixyz.com/api/lib/?id=0000475103": "200", 
    "https://ccnubox.muxixyz.com/api/lib/login/": "200", 
    "https://ccnubox.muxixyz.com/api/lib/me/": "200", 
    "https://ccnubox.muxixyz.com/api/lib/search/?keyword=\u8ba1\u7b97\u673a&page=1/": "500", 
    "https://ccnubox.muxixyz.com/api/product/": "200", 
    "https://ccnubox.muxixyz.com/api/site/": "200", 
    "https://ccnubox.muxixyz.com/api/start/": "200", 
    "https://ccnubox.muxixyz.com/api/table/": "500", 
    "https://ccnubox.muxixyz.com/api/table/5/": "403", 
    "https://grade.muxixyz.com/api/grade/search/?xnm=2016&xqm=3/": "502"
      
    }


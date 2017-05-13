#! /bin/bash
sudo redis-server /etc/redis/redis.conf &
celery worker --app monitor.celery &
celery beat --app monitor.celery &
uwsgi --ini uwsgi.ini &
python monitor.py &
echo 'running on 127.0.0.1:5001'

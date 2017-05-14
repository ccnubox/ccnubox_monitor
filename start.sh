#! /bin/bash
sudo nginx &
sudo redis-server /etc/redis/redis.conf &
celery worker --app monitor.celery &
celery beat --app monitor.celery &
uwsgi --ini app.ini &
echo 'running on 127.0.0.1:6000'

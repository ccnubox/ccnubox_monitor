#! /bin/bash
sudo nginx &
sudo redis-server /etc/redis/redis.conf &
celery worker --app monitor.celery &
celery beat --app monitor.celery &
uwsgi --ini uwsgi.ini &


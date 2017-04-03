#! /bin/bash
sudo redis-server /etc/redis/redis.conf &
celery worker --app monitor.celery &
celery beat --app monitor.celery &
python monitor.py runserver&

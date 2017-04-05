#! /bin/bash
sudo killall -9 redis-server
killall -9 celery
killall -9 uwsgi

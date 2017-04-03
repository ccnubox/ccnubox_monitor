#! /bin/bash
sudo killall -9 redis-server
killall -9 celery
echo  'The flask has not been killed'
echo  'Please stop it by its PID if you want'

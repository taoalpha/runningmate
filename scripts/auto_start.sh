#!/bin/sh
# restart script

export IRONPYTHONPATH=/root/ironPython/External.LCA_RESTRICTED/Languages/IronPython/27/Lib

DATA_SERVER="masterServer.py"
FLASK_SERVER="slaveServer.py"

if [ $1 == 1 ]
then
  DATA_SERVER=$FLASK_SERVER
fi

echo $DATA_SERVER
# if vsync server down, then restart entire node
ps auxw | grep $DATA_SERVER | grep -v grep > /dev/null

STATUS_ONE=$?

# if flask server down, then restart entire node
ps auxw | grep app.py | grep -v grep > /dev/null

STATUS_TWO=$?

# if flask down and vsync still running
#   restart the flask

if [ $STATUS_ONE == 0 && $STATUS_TWO != 0 ]
then
    killall -9 python 
    python ~/xmate/app.py & 
fi

# if vsync down, restart everything

if [ $STATUS_ONE != 0 ]
then
    killall -9 python 
    killall -9 mono 
    killall -9 ipy
    python ~/xmate/app.py & 
    ipy ~/xmate/masterServer.py
fi

# test using request if all service are running, but some internal connection lost or error happened
SERVER_URL="192.168.99.100:4000"

HTTP_CODE=curl -s -o /dev/null -I -w "%{http_code}" $SERVER_URL
HTTP_STATUS=curl $SERVER_URL

# if flask down
if [ $HTTP_CODE != 200 ]
then
    killall -9 python 
    python ~/xmate/app.py & 
fi

# if vsync down
if [ $HTTP_STATUS != 1 ]
then
    killall -9 python 
    killall -9 mono 
    killall -9 ipy
    python ~/xmate/app.py & 
    ipy ~/xmate/masterServer.py
fi

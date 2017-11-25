PGM_NAME=alarm
Cnt=`ps -ef|grep $PGM_NAME|grep -v grep|grep -v vi|wc -l`
PROCESS=`ps -ef|grep $PGM_NAME|grep -v grep|grep -v vi|awk '{print $2}'`
if [ $Cnt -gt 0 ] ; then
    sudo kill -9 $PROCESS
fi


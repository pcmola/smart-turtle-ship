#ps -ef | grep lego_clock_world | grep -v grep | awk '{print $2}' | xargs sudo kill
PGM_NAME=lego_clock_world
Cnt=`ps -ef|grep $PGM_NAME|grep -v grep|grep -v vi|wc -l`
PROCESS=`ps -ef|grep $PGM_NAME|grep -v grep|grep -v vi|awk '{print $2}'`
if [ $Cnt -gt 0 ] ; then
    sudo kill -9 $PROCESS
fi
sudo /home/pi/c/lego_clock_init


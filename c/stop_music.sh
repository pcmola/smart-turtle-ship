#stop_music.sh
#ps -ef | grep music_jong | grep -v grep | awk '{print $2}' | xargs sudo kill
#ps -ef | grep music_book | grep -v grep | awk '{print $2}' | xargs sudo kill
#ps -ef | grep music_jing | grep -v grep | awk '{print $2}' | xargs sudo kill

PGM_NAME=music
Cnt=`ps -ef|grep $PGM_NAME|grep -v grep|grep -v vi|wc -l`
PROCESS=`ps -ef|grep $PGM_NAME|grep -v grep|grep -v vi|awk '{print $2}'`
if [ $Cnt -gt 0 ] ; then
    sudo kill -9 $PROCESS
fi



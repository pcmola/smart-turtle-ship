#ps -ef | grep lego_clock_world | grep -v grep | awk '{print $2}' | xargs sudo kill
#ps -ef | grep music_ | grep -v grep | awk '{print $2}' | xargs sudo kill
#clock stop
/home/pi/c/stop_clock_led.sh

#music stop
/home/pi/c/stop_music.sh

#alarm stop
/home/pi/py/stop_alarm.sh



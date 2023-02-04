#!/bin/bash
xset s noblank
xset s off
xset -dpms

unclutter -idle 0.5 -root &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/$USER/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/$USER/.config/chromium/Default/Preferences

#/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://localhost/ &

#while true; do
#    xdotool keydown ctrl+Next; xdotool keyup ctrl+Next;
    #sleep 15
#done
	
#xdotool keydown ctrl+r; xdotool keyup ctrl+r;

echo Starting script...

LOGENTRY=`date +"%d-%m-%Y %T"`
echo "$LOGENTRY Driver startup start" >> /var/www/Tjekind/logs/log.txt

#sleep 60
#cd /
#cd home/pi/Desktop
#exec /usr/bin/python -u /var/www/Tjekind/driver/linux/nfc-reader3.py
exec /usr/bin/python -u /home/pi/Desktop/nfc-reader3.py
#cd /

EXITENTRY=`date +"%d-%m-%Y %T"`
echo "$EXITENTRY Driver startup exit" >> /var/www/Tjekind/logs/log.txt

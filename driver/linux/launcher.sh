#!/bin/bash
echo Starting script...

LOGENTRY=`date +"%d-%m-%Y %T"`
echo "$LOGENTRY Driver startup" >> /var/www/Tjekind/logs/log.txt

#sleep 60
cd /
cd home/karsten/Desktop
exec /usr/bin/python -u /var/www/Tjekind/driver/linux/nfc-reader3.py
cd /

EXITENTRY=`date +"%d-%m-%Y %T"`
echo "$EXITENTRY Driver startup exit" >> /var/www/Tjekind/logs/log.txt


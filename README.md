# Tjekind

Vores egen producerede tjek ind system. Er skrevet i php og driver til at læse kortene er skrevet i python

## Driver

Systemet har driver til NFC læseren til både Windows og Linux. Driverne er testen og fungerer på Windows 10 og Raspberry Pi linux, Raspbarian

### Python afhængigheder

## nfcpy bibliotek

Dokumentation: <https://nfcpy.readthedocs.io/en/latest/modules/clf.html>

Driveren gør brug af Python biblioteket: nfcpy

Det nemmeste er at følge vejledning på første opsætning af

    pip install -U nfcpy

    Collecting nfcpy
      Downloading nfcpy-1.0.3-py3-none-any.whl (186 kB)
         |████████████████████████████████| 186 kB 273 kB/s 
    Collecting libusb1
      Downloading libusb1-2.0.1-py3-none-win_amd64.whl (138 kB)
         |████████████████████████████████| 138 kB 409 kB/s 
    Collecting pydes
      Downloading pyDes-2.0.1.tar.gz (9.9 kB)
    Collecting ndeflib
    Collecting ndeflib
      Downloading ndeflib-0.3.3-py2.py3-none-any.whl (56 kB)
         |████████████████████████████████| 56 kB 962 kB/s
    Collecting pyserial
      Downloading pyserial-3.5-py2.py3-none-any.whl (90 kB)
         |████████████████████████████████| 90 kB 579 kB/s
    Using legacy 'setup.py install' for pydes, since package 'wheel' is not installed.
    Installing collected packages: pyserial, pydes, ndeflib, libusb1, nfcpy
        Running setup.py install for pydes ... done
    Successfully installed libusb1-2.0.1 ndeflib-0.3.3 nfcpy-1.0.3 pydes-2.0.1 pyserial-3.5

## libusb1 bibliotek

libusb burde blive installeret sammen med nfcpy. Hvis ikke kandu se på:
<https://github.com/vpelletier/python-libusb1>

## pynput biblioteket

Se nærmere dokumentation på: <https://pynput.readthedocs.io/en/latest/>

    pip install pynput

```

Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting pynput
  Downloading https://www.piwheels.org/simple/pynput/pynput-1.7.6-py2.py3-none-any.whl (79 kB)
     |████████████████████████████████| 79 kB 546 kB/s 
Collecting evdev>=1.3
  Downloading evdev-1.6.1.tar.gz (26 kB)
Requirement already satisfied: six in /usr/lib/python3/dist-packages (from pynput) (1.16.0)
Collecting python-xlib>=0.17
  Downloading https://www.piwheels.org/simple/python-xlib/python_xlib-0.33-py2.py3-none-any.whl (182 kB)
     |████████████████████████████████| 182 kB 844 kB/s 
Building wheels for collected packages: evdev
  Building wheel for evdev (setup.py) ... done
  Created wheel for evdev: filename=evdev-1.6.1-cp39-cp39-linux_aarch64.whl size=83633 sha256=c1a305ca361af160d6d2380bb04e4d3cb6effd7c7a7c6b5dc89cf4d4a44c21d3
  Stored in directory: /home/pi/.cache/pip/wheels/d9/dc/a9/bd9d84b0819a9858095ba3c033bddf84c9a6d8b360fe0a3caf
Successfully built evdev
Installing collected packages: python-xlib, evdev, pynput
Successfully installed evdev-1.6.1 pynput-1.7.6 python-xlib-0.33

```

Python scriptet er opgraderet fra at kører Python2 og har fungerer med de seneste opdateringer i forhold til NFC læseren.<br />
Det kan nogle gange betale sig at genstarte scriptet.

Der er lagt et opstarts script i bootup<br />
[TODO] Hvordan opsætter man cronjob til at igang sætte driver- og python fortolker script

## Backend

### Opsætning af service

    sudo nano /lib/systemd/system/kiosk.service

```

[Unit]
Description=Chromium Kiosk
Wants=graphical.target
After=graphical.target

[Service]
Environment=DISPLAY=:0.0
Environment=XAUTHORITY=/home/pi/.Xauthority
Type=simple
ExecStart=/bin/bash /home/pi/Desktop/kiosk.sh
Restart=on-abort
User=pi
Group=pi

[Install]
WantedBy=graphical.target

```

service filen skal sættes til at starte ved boot
    sudo systemctl enable kiosk.service

og så skal service startes
    sudo systemctl start kiosk
    

## Backend

Installeret eks. Apache server som er i stand til at køre php-filer.

  Webserver
  Apache/2.4.38 (Raspbian)
  Databaseklientversion: libmysql - mysqlnd 5.0.12-dev - 20150407 - $Id: 7cc7cc96e675f6d72e5cf0f267f48e167c2abb23 $
  PHP-udvidelse: mysqliDokumentation curlDokumentation mbstringDokumentation
  PHP-version: 7.3.11-1~deb10u1

Der er lavet et opstart script som kører efter boot sekvensen.

## Database

Databaseklientversion: libmysql - mysqlnd 5.0.12-dev - 20150407 - $Id: 7cc7cc96e675f6d72e5cf0f267f48e167c2abb23 $
Til database er der brugt MySQL. Den kører stadig i sin gamle version: 0.00.

  Database-server
  Server: Localhost via UNIX socket
  Servertype: MariaDB
  Serverversion: 10.3.22-MariaDB-0+deb10u1 - Raspbian 10
  Protokolversion: 10
  Bruger: skp@localhost
  Servers tegnsæt: UTF-8 Unicode (utf8)

phpMyAdmin
  Versionsinformation: 4.6.6deb5

# Apache webserver

Apache/2.4.38 (Raspbian)

# PHP

PHP-udvidelse: mysqliDokumentation curlDokumentation mbstringDokumentation
PHP-version: 7.3.11-1~deb10u1

# Hardware krav

Der er krav til at bruge, det eneste som driveren understøtter nu.

# Installering på Raspberry Pi

Gå til home dir for websiden<br />
    cd /var/www/

Nu kan koden installeres med:<br />
    sudo git clone <https://github.com/AARHUS-TECH/Tjekind.git>

```
Cloning into 'Tjekind'...
remote: Enumerating objects: 396, done.
remote: Counting objects: 100% (396/396), done.
remote: Compressing objects: 100% (227/227), done.
remote: Total 396 (delta 173), reused 358 (delta 154), pack-reused 0
Receiving objects: 100% (396/396), 23.06 MiB | 1.13 MiB/s, done.
Resolving deltas: 100% (173/173), done.
```

Til sidst åbnes Apache konfigurations fil og ændres til at pege på vores hjemmeside:<br />

    DocumentRoot /var/www/html

ændres til

    DocumentRoot /var/www/Tjekind/html

og Apache genstartes

    sudo service apache2 restart

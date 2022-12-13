#! /usr/bin/env python
import os
from threading import Thread
import time
import nfc
from pynput.keyboard import Controller, Key

keyboard = Controller() # Initiates keykoard keystrokes


def fullscreen(delay):
    time.sleep(delay)
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)


def browser_start():
    threadFullScreen = Thread(target=fullscreen, args=(4, ))
    threadFullScreen.start() 
    os.system("chromium-browser --start-fullscreen --disable-infobars --disable-pinch --overscroll-history-navigation=0 --kiosk --no-sandbox --allow-insecure-localhost --app=\"http://localhost\"")


def on_connect(tag):
    if isinstance (tag, nfc.tag.tt2.Type2Tag): # If tag equals nfc type tag (Type2Tag = nfc)
        nfc_tag = str(tag)[12:14]+'-'+str(tag)[14:16]+'-'+str(tag)[16:18]+'-'+str(tag)[18:20] # Creates string = XX-XX-XX-XX
        print (nfc_tag)
        keyboard.type(nfc_tag) # Types the nfc input to cursor focus
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Enter keystroke has been emulated
        return True # Beep when returned true
    else:
        return False
        

rdwr_options = { # Initiate functions
                'on-connect': on_connect,
                'beep-on-connect': True,
                }


def main():
    with nfc.ContactlessFrontend('usb:072f:2200') as clf: # communicates with (usb:072f:2200) ACR122U id
        print ("ACR112 started...")
        # create a thread
        threadBrowser = Thread(target=browser_start, args=())
        threadBrowser.start()
        #thread.start_new_thread(browser_start, ())
        while clf.connect(rdwr=rdwr_options): # Connects with (rdwr_options) # edit
            time.sleep(2)


main() # Starts the script
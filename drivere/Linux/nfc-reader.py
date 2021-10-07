#! /usr/bin/env python

import os
import thread
import time

import nfc.clf
from pynput.keyboard import Controller, Key

keyboard = Controller() # Initiates keykoard keystrokes

def fullscreen(delay):
    time.sleep(delay)
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)


def browser_start():
    thread.start_new_thread(fullscreen, (4,))
    os.system("chromium-browser --start-fullscreen --disable-infobars --disable-pinch --overscroll-history-navigation=0 --kiosk --no-sandbox --allow-insecure-localhost --app=\"https://localhost\"")


def on_connect(tag):
    if isinstance (tag, nfc.tag.tt2.Type2Tag): # If tag equals nfc type tag (Type2Tag = nfc)
        nfc_tag = str(tag)[12:14]+'-'+str(tag)[14:16]+'-'+str(tag)[16:18]+'-'+str(tag)[18:20] # Creates string = XX-XX-XX-XX
        print nfc_tag
        keyboard.type(nfc_tag) # Types the nfc input to cursor focus
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        # Enter keystroke has been emulated
        return True # Beep when returned true
        

rdwr_options = { # Initiate functions
                'on-connect': on_connect,
                'beep-on-connect': True,
                }

def run():
    with nfc.ContactlessFrontend('usb:072f:2200') as clf: # communicates with (usb:072f:2200) ACR122U id
        print"ACR112 started..."
        thread.start_new_thread(browser_start, ())
        while clf.connect(rdwr=rdwr_options): # Connects with (rdwr_options) # edit
            time.sleep(2)

    
run() # Starts the script

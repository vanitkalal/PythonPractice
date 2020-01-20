#vanitk
#This program takes and address from commad line or from the clipboard. Then opens it in google maps.

import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

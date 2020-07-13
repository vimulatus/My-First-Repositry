#! /usr/bin/env python3

import webbrowser, sys, pyperclip

# to store the command line arguments
sys.argv 
# mapit.py Vasu Mittal will give ['mapit.py', 'Vasu', 'Mittal']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    # will return 'Vasu Mittal'
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

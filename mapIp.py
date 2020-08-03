import sys, os, webbrowser, pyperclip

if len(sys.argv[1])>1:
    adress = "".join(sys.argv[1:])
else:
    adress = pyperclip.paste()

dest = "https://www.google.ru/maps/place/"
webbrowser.open(dest+adress)
while True:    
    one_more = input(r"One more? => Ctrl+C kills program ")
    webbrowser.open(dest+one_more)


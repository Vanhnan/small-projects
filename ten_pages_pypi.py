import sys, webbrowser, pyperclip
import requests
from bs4 import BeautifulSoup

res = ""
if len(sys.argv[1:])>1:
    for i in range(len(sys.argv[1:])): 
        res+=sys.argv[1:][i]+" "
elif len(sys.argv[1:])==1:
    res+=sys.argv[1]
else:
    res = pyperclip.paste()

page = requests.get("https://pypi.org/search/?q="+res)
soup = BeautifulSoup(page.text, "html.parser")
link = soup.select('.package-snippet')
for i in link:
    webbrowser.open("https://pypi.org/"+i.get("href"))

import requests, os
from bs4 import BeautifulSoup

path = "C:\\Users\\v4h4\\xkcd"
url = "https://xkcd.com/"
while not url.endswith("2300"):    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    image = soup.select("#comic > img")
    img_url = "https:"+image[0].get("src")
    img_page = requests.get(img_url)
    file_name = img_url.split("/")[-1]
    with open(os.path.join(path, file_name), "wb") as f:
        for i in img_page.iter_content(100000):
            f.write(i)

    prev_link = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com"+prev_link.get("href")

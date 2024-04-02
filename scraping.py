import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
import json

web = requests.get("https://www.republika.co.id/").text

soup = BeautifulSoup(web, "html.parser")

data = []

file = open("data.json", "w")

info = soup.find_all("li", class_="list-group-item list-border conten1")

for infoNews in info:
    title = infoNews.h3.text
    category = infoNews.find("span", class_="kanal-info").text
    uploadTime = infoNews.find("div", class_="date").text.split("-")
    uploadTimeClear = uploadTime[1].strip()
    scrapingTime = dt.now().strftime("%d %b %Y %H:%M:%S")

    data.append(
        {
            "Judul": title,
            "Kategori": category,
            "Publish": uploadTimeClear,
            "Scraping": scrapingTime,
        }
    )

jdumps = json.dumps(data)
file.writelines(jdumps)

file.close()

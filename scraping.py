# File: scraping.py
# Import package untuk scraping website
import requests
from bs4 import BeautifulSoup

# Import package untuk kebutuhan penulisan file
from datetime import datetime as dt
import json
import os

# Request ke website
web = requests.get("https://www.republika.co.id/").text
# Extract konten menjadi objek BeautifulSoup
soup = BeautifulSoup(web, "html.parser")

# Cek apabila data sudah ada atau belum,
# ini bertujuan untuk kebutuhan append file nantinya
if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
    with open("data.json", "r") as file:
        data = json.load(file)
else:
    data = []

# Sebuah array yang menampung judul-judul yang sudah ada di dalam file
existing_titles = [item["Judul"] for item in data]

info = soup.find_all("li", class_="list-group-item list-border conten1")

for infoNews in info:
    title = infoNews.h3.text
    # Apabila judul tidak ditemukan, maka append
    if title not in existing_titles:
        category = infoNews.find("span", class_="kanal-info").text
        uploadTime = infoNews.find("div", class_="date").text.split("-")
        uploadTimeClear = uploadTime[1].strip()
        scrapingTime = dt.now().strftime("%d %b %Y %H:%M:%S")
        linkBerita = infoNews.find("a")["href"]

        data.append(
            {
                "Judul": title,
                "Kategori": category,
                "Publish": uploadTimeClear,
                "Scraping": scrapingTime,
                "Link": linkBerita,
            }
        )

# Menulis data ke file json
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

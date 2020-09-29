### A script to check for new announcements on the site of Dept of Physics, UoP and send notification via pushover

import requests, http.client, urllib, sys, time
from bs4 import BeautifulSoup

r = requests.get("http://www.physics.upatras.gr/index.php?page=newsNews/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content

soup=BeautifulSoup(c,"html.parser")


all=soup.find_all("div",{"class":"wrapper col3"})



all[0].find("div",{"id":"content"})
hub=[]
#print(all)
while True:
    for item in all:
        b=item.find("a",{"class":"newsFirstTitleWhite"}).text
        if b in hub:
            print("Δεν υπάχουν νέες ανακοινώσεις")
        else:
            hub.clear()
            hub.append(b)
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
            urllib.parse.urlencode({
                "token": "my_token",
                "user": "my_user",
                "message": b,
                "title": "Physics",
                "url": "http://www.physics.upatras.gr/index.php?page=newsNews/",
                "url_title": "announcement's url",
            }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()
    time.sleep(1800)



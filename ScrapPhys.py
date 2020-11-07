import requests, http.client, urllib, sys, time
from bs4 import BeautifulSoup

r = requests.get("http://www.physics.upatras.gr/index.php?page=newsNews/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content

soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("div",{"class":"wrapper col3"})
all[0].find("div",{"id":"content"})
for item in all:
    b=item.find("a",{"class":"newsFirstTitleWhite"}).text

f= open("Announcements.txt","r+")

    
with open("Announcements.txt") as f:
    if b in f.read():
        print("Δεν υπάχουν νέες ανακοινώσεις")
    else:
        f = open('Announcements.txt', 'r+')
        f.truncate(0)
        f = open('Announcements.txt', 'a+')
        f.write(b)
        f.close()

        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": "my token",
            "user": "my user",
            "message": b,
            "title": "Physics",
            "url": "http://www.physics.upatras.gr/index.php?page=newsNews/",
            "url_title": "url ανακοίνωσης",
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()
    

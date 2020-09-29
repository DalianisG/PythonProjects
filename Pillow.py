from datetime import datetime
import requests, http.client, urllib, sys, time



time = datetime.now()
d=time.strftime("%d/%m/%Y %H:%M:%S")





conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
urllib.parse.urlencode({
    "token": "My_Token",
    "user": "My_User",
    "message":"Take your Pillow",
    "title": "Pillow",
}), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()


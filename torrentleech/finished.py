from app import login, seeding_torrents, pushover_notification, check_number_of_current_uploads
from credentials import username, password

#login to TL ---------------
#Go to seeding
#Sort
#If ... = 6 days -> send pushover
#every 1 hour!

login(username,password) 


for i in range(check_number_of_current_uploads()):
    seeding_time = seeding_torrents(i)
    if '6 days' in seeding_time:
        pushover_notification("Go delete a torrent")
        break


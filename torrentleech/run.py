from app import login, check_upload_counter, pushover_notification, thank_uploader, check_thank_counter, write_a_comment,check_comment_counter
from credentials import username, password, random_list
import random

k=2 #random.choice(random_list)
print(k)
login(username,password) 
upload = check_upload_counter()
for i in range(k):
    thank_uploader(random.choice(random_list))
    write_a_comment()

thanks_counter = check_thank_counter()
comment_counter = check_comment_counter()

pushover_notification("Current upload is: " + upload + "\n" + 
"Times I am going to thank-comment: " + str(k) + "\n" + 
"Thank uploader: " + thanks_counter + "\n" + 
"Comments Counter: " + comment_counter)



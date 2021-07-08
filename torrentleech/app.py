from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import http.client, urllib, time, random
from credentials import random_list, Comments, Pushover_token, Pushover_user


def login(username,password):
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_path = "/usr/bin/chromedriver"

    driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
    driver.get("https://www.torrentleech.org/") #Go to torrentleech

    driver.find_element_by_name("username").send_keys(username) #Add username
    time.sleep(random.choice(random_list)) 

    driver.find_element_by_name("password").send_keys(password) #Add password
    time.sleep(random.choice(random_list))

    driver.find_element_by_xpath("//button[contains(@type, 'submit')]").click() #click login button
    time.sleep(random.choice(random_list))


def check_upload_counter():
    mplah = driver.find_elements_by_xpath("//span[contains(@class, 'link')]")[3].text  #Check 'upload" counter
    time.sleep(random.choice(random_list))    

    return mplah


def thank_uploader(k):
    driver.find_element_by_xpath("//a[contains(@href, '/torrents/browse/index')]").click() #Click "Browse"
    time.sleep(random.choice(random_list))

    driver.find_elements_by_xpath("//div[contains(@class, 'name')]")[random.choice(random_list)].click() #Click a random torrent
    time.sleep(random.choice(random_list))
    
    driver.find_element_by_xpath("//button[contains(@class, 'thankYouButton ')]").click() #Click "thank you"
    time.sleep(random.choice(random_list))


def check_thank_counter():
    driver.find_elements_by_xpath("//span[contains(@class, 'link')]")[6].click() # Go to achievements
    time.sleep(random.choice(random_list))

    thanks_counter =driver.find_elements_by_xpath("//tr[contains(@class, 'cat9')]/td[contains(@align, 'center')]")[10].text #Check 'thank you" counter
    return thanks_counter


def write_a_comment():
    driver.find_element_by_id("add_comments_textarea").send_keys(random.choice(Comments)) #write comment
    time.sleep(random.choice(random_list))

    driver.find_element_by_xpath("//button[contains(@class, 'add-comment')]").click() #Click "add comment"
    time.sleep(random.choice(random_list))


def check_comment_counter():
    driver.find_elements_by_xpath("//span[contains(@class, 'link')]")[6].click() # Go to achievements
    time.sleep(random.choice(random_list))

    comment_counter =driver.find_elements_by_xpath("//tr[contains(@class, 'cat5')]/td[contains(@align, 'center')]")[10].text #Check 'thank you" counter
    driver.close()
    return comment_counter


def seeding_torrents(i):
    driver.find_elements_by_xpath("//span[contains(@class, 'link')]")[3].click()  #click upload
    time.sleep(1)

    driver.find_element_by_xpath("//th[contains(@title, 'Seeding Time')]").click()  #click 'sort'
    time.sleep(1)

    xxxxx = driver.find_elements_by_xpath("//td[contains(@title, 'Seeding Time')]")[i].text  
    time.sleep(1)
    return xxxxx


def check_number_of_current_uploads(): #Uploads minus my 100 standard torrents
    number_of_uploads = int(driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/span[2]/span[1]/div[1]").text[-4:-1]) -100
    time.sleep(1)

    return number_of_uploads


def pushover_notification(message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": Pushover_token,
        "user": Pushover_user,
        "message": message,
        "title": "TorrentLeech",
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
